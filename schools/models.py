from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_info = models.CharField(max_length=50)