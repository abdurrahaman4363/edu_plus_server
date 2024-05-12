from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.StudentListCreateAPIView.as_view(),
         name='student-create'),
    path('students/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view(),
         name='student-retrieve-update-destroy'),
]
