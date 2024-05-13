from django.db import models
from Course.models import *

class Exam(models.Model):
    COURSE_CHOICES = [
        (1, '1st Term'),
        (2, 'Mid Term'),
        (3, 'Final'),
    ]
    exam_type = models.IntegerField(choices=COURSE_CHOICES)
    date = models.DateField()
    duration = models.PositiveIntegerField()
    subjects = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.exam_type} Exam - {', '.join(subject.name for subject in self.subjects.all())}"