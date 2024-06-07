from django.contrib import admin

# Register your models here.
from .models import Client,Comment,Todolist

admin.site.register(Client)
admin.site.register(Comment)
admin.site.register(Todolist)

