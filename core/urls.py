from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('files', views.FileViewSet)

urlpatterns = router.urls