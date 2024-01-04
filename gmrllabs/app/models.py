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

class Packages(models.Model):from django.db import models


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

class Ayushsilverplan(models.Model):
      name=models.CharField(max_length=50)
      t1=models.CharField(max_length=50)
      t2=models.CharField(max_length=50)
      t3=models.CharField(max_length=50)
      t4=models.CharField(max_length=50)
      t5=models.CharField(max_length=50)
      cost=models.CharField(max_length=50)

      image=models.ImageField(upload_to='img')
      package=models.ForeignKey(Packages,on_delete=models.CASCADE)
      image=models.ImageField(upload_to='img')
      description=models.CharField(max_length=255)

      def ___str__(self):
            return self.description

class Blog(models.Model):
      image=models.ImageField(upload_to='img')
      description=models.CharField(max_length=255)
      def ___str__(self):
            return self.description

class Branches(models.Model):
      images=models.ImageField(upload_to='img')
      descriptions=models.CharField(max_length=255)
      
class Gallery(models.Model):
      images=models.ImageField(upload_to='img')

class Ayushsilverplan(models.Model):
      name=models.CharField(max_length=50)
      t1=models.CharField(max_length=50)
      t2=models.CharField(max_length=50)
      t3=models.CharField(max_length=50)
      t4=models.CharField(max_length=50)
      t5=models.CharField(max_length=50)
      cost=models.CharField(max_length=50)

      image=models.ImageField(upload_to='img')
      package=models.ForeignKey(Packages,on_delete=models.CASCADE)

class Sub_blog(models.Model):
      image=models.ImageField(upload_to='img')
      heading1=models.CharField(max_length=255)
      heading2=models.CharField(max_length=255)
      heading3=models.CharField(max_length=255)
      paragraph2=models.CharField(max_length=255)
      paragraph3=models.CharField(max_length=255)
      blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
