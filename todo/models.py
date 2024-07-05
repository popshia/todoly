from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Todos(models.Model):
    class Meta:
        ordering = ("title",)

    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project, related_name="todos", on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="todo_photo", blank=True, null=True)
    due_date = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    add_by = models.ForeignKey(User, related_name="add_by", on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
