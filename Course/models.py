from django.db import models
from teachers.models import Teacher
from students.models import Student

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    image = models.ImageField (upload_to='Course/image')
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
