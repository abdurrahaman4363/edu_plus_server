from django.db import models
from classes.models import *

# Create your models here.
GENDER_OPTION = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]


class Student(models.Model):
    classes =models.ForeignKey(Classes, verbose_name="Classes", on_delete=models.CASCADE, default=1)
    user = models.OneToOneField(User,on_delete=models.CASCADE ,null=True )
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.CharField(max_length=200)
    gender = models.CharField(choices=GENDER_OPTION, max_length=50)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to="students/image/",blank=True)
    date_of_join = models.DateField(auto_now_add=True)
    parent_name = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


