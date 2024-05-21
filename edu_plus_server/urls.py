

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

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
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)