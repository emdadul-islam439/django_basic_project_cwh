import email
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    desc = models.TextField()
    date = models.DateField() 
    
    def __str__(self) -> str:
        return f"Name: [ {self.name} ] -    Desc: [ {self.desc} ]"
