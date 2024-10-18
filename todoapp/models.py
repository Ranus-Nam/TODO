from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField(blank=False, max_length=900)
    completed = models.BooleanField(default=False)
