from django.db import models

# Create your models here.
from django.db import models
from django import forms
from django.contrib.auth import get_user_model;
from django.contrib.auth.models import User


User = get_user_model();
class Doc(models.Model):
    doc = models.OneToOneField(User, on_delete=models.CASCADE)
    isDoc = models.BooleanField(default=True)
class Patient(models.Model):
    patient = models.OneToOneField(User,on_delete=models.CASCADE)
    weight = models.IntegerField(default=0);
    previous_symptoms=models.CharField(max_length=112,default='')
    allergies = models.TextField(max_length=500, default='')
    gender = models.CharField(max_length=23, default='')
