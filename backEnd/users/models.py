from django.db import models

from collections import defaultdict
from django.db import models
from django.contrib.auth.models import User


class Design(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class User(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='userimage/', blank=True)
    Name = models.CharField(max_length=100, blank=False)
    Lastname = models.CharField(max_length=100,blank=False)
    Id = models.CharField(max_length=100,blank=False)
    Password = models.CharField(max_length=100, blank=False)
    Phone = models.IntegerField(blank=True)
    Email = models.EmailField(max_length=100, blank=True)
    Address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.Id, self.Image.file