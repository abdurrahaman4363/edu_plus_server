from django.db import models
from teachers.models import Teacher
from django.utils import timezone

class Assignment(models.Model):
    Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField()
    Marks = models.PositiveIntegerField()
    
    def __str__(self):
        return self.Title
    
    # is it ok 