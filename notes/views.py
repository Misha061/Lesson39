from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from .forms import NoteForm
from .models import Note, NoteType

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

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("note_list")

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("note_list")

class NoteDeleteView(DeleteView):
    model = Note
    template_name = "note_delete.html"
    success_url = reverse_lazy("note_list")