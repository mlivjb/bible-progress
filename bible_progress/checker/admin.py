from django.contrib import admin

# Register your models here.
from .models import Main, Book, ReadChapter

admin.site.register(Main)
admin.site.register(Book)
admin.site.register(ReadChapter)