from django.db import models


class Todo(models.Model):
    description = models.CharField('Описание заметки', max_length=100)
    is_done = models.BooleanField(default=False, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True)