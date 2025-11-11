from django.urls import path
from .views import note_view

urlpatterns = [
    path('notes/', note_view, name='notes'),

]