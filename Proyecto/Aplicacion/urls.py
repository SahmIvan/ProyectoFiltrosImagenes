from django.urls import path
from . import views

urlpatterns = [
    path('Aplicacion/', views.test_view, name='members'),
]