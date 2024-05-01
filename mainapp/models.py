from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=255)
    file = models.ImageField(upload_to='images/')

class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='videos/')

class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    subject=models.CharField(max_length=255)
    message=models.TextField(blank=True)


