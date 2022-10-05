from django.db import models
from django.utils import timezone


class Categories(models.Model):
    name = models.CharField(max_length=50)

    class meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Todolist(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    cre_date = models.DateField(default=timezone.now().strftime('%Y-%m-%d'))
    due_date = models.DateField(default=timezone.now().strftime('%Y-%m-%d'))
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class meta:
        ordering = ['due_date']

    def __str__(self):
        return self.title
