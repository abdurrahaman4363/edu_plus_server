from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'analytics', views.AnalyticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
