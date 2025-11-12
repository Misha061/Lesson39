from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    reminder = models.DateField()

    def __str__(self):
        return f"{self.title}"

class NoteType(models.Model):
    title = models.CharField(max_length=100)
    notes = models.ForeignKey(Note, on_delete=models.CASCADE)


