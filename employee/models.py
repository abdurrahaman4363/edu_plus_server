from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employee(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="employee/images/")
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name}"
