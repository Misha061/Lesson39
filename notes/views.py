from django.shortcuts import render
from django.http import HttpResponse

def note_view(request):
    return HttpResponse("Hello from Notes app")
