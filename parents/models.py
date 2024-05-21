from django.db import models
from students.models import Student
from django.contrib.auth.models import User

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100 ,null = True)
    student_ID = models.OneToOneField(Student, on_delete=models.CASCADE, null=True, related_name='parent_student')
    parent_ID = models.AutoField(primary_key=True)
    # student_name = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, related_name='parent_student_name')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    relationship_to_Student = models.CharField(max_length=100)

    def __str__(self):
       
        return self.student.name if self.student else 'Unknown'
