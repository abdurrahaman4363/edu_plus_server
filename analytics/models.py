from django.db import models
from django.contrib.auth.models import User
from teachers.models import Teacher
# from admin.models import Admin

class Analytics(models.Model):
    analytics_ID = models.AutoField(primary_key=True)
    # admin_ID = models.ForeignKey(Admin, on_delete=models.CASCADE)
    teacher_ID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    report_name = models.CharField(max_length=100)
    date_Generated = models.DateTimeField(auto_now_add=True)
    metrics = models.TextField()

    def __str__(self):
        return self.report_name
