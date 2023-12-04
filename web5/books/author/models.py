from django.db import models

# Create your models here.
class  Author(models.Model):
    name=models.CharField(max_length=255)
    
class Views(models.Model):
    name=models.CharField(max_length=255)