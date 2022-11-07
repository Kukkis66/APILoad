from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('API', views.FileViewSet)

urlpatterns = [ 
    path('signup/', views.SignUp, name='signup'),

] 

urlpatterns += router.urls