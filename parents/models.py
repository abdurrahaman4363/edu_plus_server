from django.db import models
from students.models import Student
from django.contrib.auth.models import User

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    parent_ID = models.AutoField(primary_key=True)
    student_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    relationship_to_Student = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name
