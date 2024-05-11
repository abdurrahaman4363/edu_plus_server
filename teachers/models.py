from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('Others', 'Other'),
)
class Teacher(models.Model):
    teacher_ID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    gender = models.CharField(max_length=8, choices= GENDER_CHOICES)
    address = models.TextField()
    date_of_join = models.DateField()

    def __str__(self):
        return self.user.first_name


