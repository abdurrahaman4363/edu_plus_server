

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("employee/", include("employee.urls")),
    path("teachers/", include("teachers.urls")),
    path("parents/", include("parents.urls")),
    path("grade/", include("grade.urls")),
    path("analytics/", include("analytics.urls")),
    path("assignment/", include("Assignment.urls")),
    path("courses/",include("Course.urls")),
    path("student/",include("students.urls")),
    path("classes/",include("classes.urls")),
    path("attendences/",include("attendences.urls")),
]
