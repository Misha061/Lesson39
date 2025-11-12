from django.shortcuts import render
from django.http import HttpResponse
from .models import Note, NoteType
def note_view(request):
    return HttpResponse("Hello from Notes app")

# def remarks(request): ### Lesson39
#
#     return render(request, "lesson39.html", {"name":"Misha", "notes" : [{"text" : "Make homework"}, {"text":"Go to the shop"}]})

def notes_view(request):
    notes = Note.objects.all()
    note_types = NoteType.objects.all()
    return render(request, "lesson39.html", {"notes": notes, "note_types": note_types, "name" : "Misha"})