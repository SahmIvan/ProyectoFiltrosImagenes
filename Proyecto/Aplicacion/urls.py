from django.urls import path
from . import views

urlpatterns = [
    path('Aplicacion/', views.processImage, name='members'),
    
]