from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# https://www.youtube.com/watch?v=RbJOmgTX63M   Refer this channel

class Team(models.Model):
    name = models.CharField(max_length=250)
    users = models.ManyToManyField(User)
    
