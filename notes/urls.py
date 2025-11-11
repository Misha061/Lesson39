from django.urls import path
from .views import note_view, remarks

urlpatterns = [
    path('notes/', note_view, name='notes'),
    path("remarks/", remarks),

]