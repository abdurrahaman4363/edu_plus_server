from django.contrib import admin
from . import models

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["employee_id", "first_name", "last_name", "email", "phone_number"]

    def first_name(self, obj):
        return obj.employee.first_name

    def last_name(self, obj):
        return obj.employee.last_name

    def email(self, obj):
        return obj.employee.email


admin.site.register(models.Employee, EmployeeAdmin)
