import email
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    desc = models.CharField(max_length=2000)
    date = models.DateField() 
    
