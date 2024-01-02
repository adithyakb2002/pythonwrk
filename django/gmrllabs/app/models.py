from django.db import models


# Create your models here.
class Index(models.Model):
      name=models.CharField(max_length=50)
      email=models.EmailField()
      phone=models.CharField(max_length=10)
      message=models.TextField()

class Contact(models.Model):
      name=models.CharField(max_length=50)
      email=models.EmailField()
      phone=models.CharField(max_length=10)
      subject=models.CharField(max_length=50)
      message=models.TextField()

class Appointment(models.Model):
      name=models.CharField(max_length=50)
      email=models.EmailField()
      phone=models.CharField(max_length=10)
      message=models.TextField()
      age=models.CharField(max_length=10)
      gender=models.CharField(max_length=10)
      address=models.TextField()
      date=models.DateField(null=True)
      time=models.TimeField()

class Packages(models.Model):
      image=models.ImageField(upload_to='img')
      description=models.CharField(max_length=255)

      def ___str__(self):
            return self.description

class Blog(models.Model):
      image=models.ImageField(upload_to='img')
      description=models.CharField(max_length=255)

class Branches(models.Model):
      images=models.ImageField(upload_to='img')
      descriptions=models.CharField(max_length=255)
      
class Gallery(models.Model):
      images=models.ImageField(upload_to='img')
