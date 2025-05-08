# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('withdraw/', views.withdraw, name='withdraw'),
]