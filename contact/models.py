from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    Name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phonenumber =models.CharField(max_length=12)
    massage = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)


class Email(models.Model): 
    email = models.EmailField(max_length=255,default=True)

   