from django.db import models
from teachers.models import *

# Create your models here.
class Classes(models.Model):
    name = models.CharField(max_length=100)
    class_teacher = models.ForeignKey(Teacher, verbose_name="ClassTeacher", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
