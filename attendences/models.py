from django.db import models
from students.models import *
# Create your models here.
class Attendence(models.Model):
    student_id = models.ForeignKey(Student, verbose_name=("classattendence"), on_delete=models.CASCADE)
    date_of = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student_id.first_name} - {self.date_of}: {self.status}"
    