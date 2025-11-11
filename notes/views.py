from django.shortcuts import render
from django.http import HttpResponse

def note_view(request):
    return HttpResponse("Hello from Notes app")

def remarks(request): ### Lesson39

    return render(request, "lesson39.html", {"name":"Misha", "notes" : [{"text" : "Make homework"}, {"text":"Go to the shop"}]})

