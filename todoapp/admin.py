from django.contrib import admin
from . import models


# Register your models here.
class TodolistAdmin(admin.ModelAdmin):
    list_display = ('title', 'cre_date', 'due_date', 'content', 'category')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.Todolist, TodolistAdmin)
admin.site.register(models.Categories, CategoriesAdmin)
