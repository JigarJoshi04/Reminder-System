from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile2(models.Model):
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=100, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    username = models.CharField(max_length=100, blank=True)
    phone_no = models.IntegerField()
    gst = models.IntegerField()
    aadhar = models.IntegerField()
    pan = models.IntegerField()
    password1 = models.CharField(max_length=100, blank=True)
    password2= models.CharField(max_length=100, blank=True)
    signup_confirmation = models.BooleanField(default=False)

