from django.db import models


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
      
class Packages(models.Model):
      image=models.ImageField(upload_to='img')
      description=models.CharField(max_length=255)
class Newsevents(models.Model):
      images=models.ImageField(upload_to='img')
      descriptions=models.CharField(max_length=255)

class Gallery(models.Model):
      images=models.ImageField(upload_to='img')
      
class Subpackages(models.Model):
      packagename=models.CharField(max_length=50)

      image=models.ImageField(upload_to='img')
      package=models.ForeignKey(Packages,on_delete=models.CASCADE)

      def ___str__(self):
            return self.description
      
class Subpackagesinner(models.Model):
      Duration=models.CharField(max_length=50)
      Location=models.CharField(max_length=50)
      Price=models.CharField(max_length=50)
      package=models.ForeignKey(Packages,on_delete=models.CASCADE)
      
class Subnewsevents(models.Model):
      heading=models.CharField(max_length=50)
      paragraph=models.TextField()
      images=models.ImageField(upload_to='img')
      descriptions=models.CharField(max_length=50)
      package=models.ForeignKey(Packages,on_delete=models.CASCADE)
      
      def ___str__(self):
            return self.descriptions

class Booknow(models.Model):
      name=models.CharField(max_length=50)
      email=models.EmailField()
      phone=models.CharField(max_length=50)
      requirment=models.TextField()

class Visiting(models.Model):
      place=models.CharField(max_length=50)
      Location=models.CharField(max_length=50)
      Location1=models.CharField(max_length=50)
      description=models.TextField()
      


# Create your models here.
