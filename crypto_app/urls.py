from django.contrib import admin 
from rest_framework import routers
from django.urls import path, include
from .views import RunScraperView, ListRecordsView, DeleteRecordsView, GenerateExcelView
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('crypto_app/', include(router.urls)),
]











