from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
