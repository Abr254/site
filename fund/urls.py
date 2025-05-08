from django.urls import path
from .import views
from fund.views import spin

urlpatterns = [
    path('', views.spin, name='spin'),
]