from django.urls import path
from . import views

urlpatterns = [
    path('', views.mpesa, name='mpesa'),
    path('admin/check_balance', views.mpesa, name='check_balance'),
]