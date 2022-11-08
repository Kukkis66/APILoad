from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('API', views.FileViewSet)

urlpatterns = [ 
    path('signup/', views.SignUp, name='signup'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),



] 

urlpatterns += router.urls