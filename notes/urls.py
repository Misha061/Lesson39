from django.urls import path
from .views import note_view, notes_view

urlpatterns = [
    path('notes/', note_view, name='notes'),
    # path("remarks/", remarks),
    path('notes-output/', notes_view, name='notes_create'),

]