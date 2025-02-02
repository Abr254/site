from django.urls import path
from . import views
from .views import  register, feenax,notify
urlpatterns = [
      # Home page view (this will render the home template)
    path('', views.register, name='register'),  # Registration page
    path('login/', views.user_login, name='login'),  # Login page
    path('notify/', notify, name='notify'),  # Notification page (requires login)
    path('feenax/', feenax, name='feenax'),  # Home page after login (for authenticated users)
    # Logout view
]
