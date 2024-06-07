from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from team.models import Team

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)


class Client(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment,blank=True)
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    
class Todolist(models.Model):
    client = models.ForeignKey(Client,related_name='todolist',on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment,blank=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,related_name='todolist',on_delete=models.CASCADE)

