# from django.contrib import admin
# from . models import Todo
#
# # Register your models here.
#
# admin.site.register(Todo)

from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ['title',  'image' ]