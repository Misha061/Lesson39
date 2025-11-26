from django.contrib import admin

# Register your models here.
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'text', 'reminder')
    list_filter = ('title','reminder')
    search_fields = ('title','reminder', 'name')
    ordering = ('title',)

admin.site.register(Note, NoteAdmin)