from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from .forms import NoteForm, LoginForm, RegisterForm
from .models import Note
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Вітаємо {username}!")
                return redirect('note_list')
            else:
                messages.error(request, f"Неправильне ім'я користувача або пароль")
        return render(request, 'login.html', {"form": form})

def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'register.html', {"form": form})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Реєстрація успішна!")
            return redirect('note_list')
        return render(request, 'register.html', {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "Ви успішно вийшли із системи!")
    return redirect('login')

class NoteReadView(DeleteView):
    model = Note
    form_class = NoteForm
    template_name = "note_detail.html"

class NoteListView(ListView):
    model = Note
    form_class = NoteForm
    template_name = "note_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        reminder = self.request.GET.get('reminder')
        name_search = self.request.GET.get('name_search')
        if title:
            queryset = queryset.filter(title__icontains=title)
        if reminder:
            queryset = queryset.filter(reminder__icontains=reminder)
        if name_search:
            queryset = queryset.filter(name__icontains=name_search)

        return queryset

class NoteCreateView(LoginRequiredMixin , CreateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("note_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteUpdateView(UserPassesTestMixin,UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("note_list")

    def get_success_url(self):

        return reverse_lazy('note_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        note = self.get_object()
        return note.user == self.request.user

class NoteDeleteView( UserPassesTestMixin,DeleteView):
    model = Note
    template_name = "note_delete.html"
    success_url = reverse_lazy("note_list")

    def test_func(self):
        note = self.get_object()
        return note.user == self.request.user