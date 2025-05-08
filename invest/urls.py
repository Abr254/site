# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('invest/', views.invest, name='invest'),
]