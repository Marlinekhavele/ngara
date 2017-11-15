from __future__ import unicode_literals

from django.db import models
from django import forms

import datetime

# Create your models here.
class Index(models.Model):
    service = models.CharField(max_length=30,default="General cleaning")
    # context =models.TextField()
    timestamp = models. DateTimeField(default=datetime.datetime.now)
    picture = models.ImageField(default='default.png')
    
class About(models.Model):
    
    service = models.CharField(max_length=30,default="general")
    # context =models.TextField()
    timestamp = models. DateTimeField(default=datetime.datetime.now)
    
class Service(models.Model):
    service = models.CharField(max_length=30, default='SOME STRING')
    # context =models.TextField()
    timestamp = models. DateTimeField(default=datetime.datetime.now)
    
class Contact(models.Model):
    firstName = models.CharField(max_length=30,default="firstname")
    lastName = models.CharField(max_length=30, default="lastname")
    email = models.EmailField(max_length=70,blank=True)
    password = forms.CharField(widget=forms.PasswordInput) 
    estate = models.CharField(max_length=100,default="estate")
    Location = models.CharField(max_length=100,default="location")

    

