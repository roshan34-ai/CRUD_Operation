from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll_no = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    mob_no = models.CharField(max_length=12)
