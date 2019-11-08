from django.db import models

# Create your models here.
from django.db import models
from django import forms
from django.contrib.auth import get_user_model;
from django.contrib.auth.models import User


User = get_user_model();
class Doc(models.Model):
    doc = models.ForeignKey(User, unique=True,on_delete=models.CASCADE)
    isDoc = models.BooleanField(default=True)
class Patient(models.Model):
    patient = models.ForeignKey(User,unique=True,on_delete=models.CASCADE)
