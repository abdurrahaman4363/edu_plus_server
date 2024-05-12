from django.db import models
from students.models import Student

class Grade(models.Model):
    drade_ID = models.AutoField(primary_key=True)
    student_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade_Name = models.CharField(max_length=100)
    grade_Point = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.grade_Name
