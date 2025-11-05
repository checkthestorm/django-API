from django.contrib.auth.models import User
from django.db import models

class TaskModel(models.Model):
    taskOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.description
