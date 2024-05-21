from django.urls import path
from .views import UserRegistrationView, UserLoginView,Userlist
from django.urls import path,include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'users', Userlist)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login')
   
]