from django.db import models

class Course(models.Model):
    course =models.CharField(max_length=255)
    image  =models.ImageField(upload_to='images/')
class New(models.Model):
     title =models.CharField(max_length=255)
     image  =models.ImageField(upload_to='images/')
     summary =models.TextField()
class Service(models.Model):
     title =models.CharField(max_length=255)
     image  =models.ImageField(upload_to='images/')
     summary =models.TextField()
