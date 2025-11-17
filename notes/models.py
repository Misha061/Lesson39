from django.db import models
from django.urls import reverse

class Note(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    reminder = models.DateField()

    def __str__(self):
        return f"{self.title}"
    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk': self.pk})

class NoteType(models.Model):
    title = models.CharField(max_length=100)
    notes = models.ForeignKey(Note, on_delete=models.CASCADE)


