from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# AKA DATABASE

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "todolist", null = True)
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete = models.CASCADE)
    text = models.CharField(max_length = 300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
    
class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "entrylist", null = True)
    entry_title = models.CharField(max_length=200)
    entry_date = models.DateField()
    entry_content = models.TextField()

    def __str__(self):
        return self.entry_title

