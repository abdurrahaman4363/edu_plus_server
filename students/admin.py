from django.contrib import admin
from . models import Student
# Register your models here.


class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email',
                    'gender', 'address', 'phone', 'date_of_join', 'parent_name']


admin.site.register(Student, StudentModelAdmin)
