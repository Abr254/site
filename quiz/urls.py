from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),  # List of all available quizzes
    path('quiz/<int:quiz_id>/', views.start_quiz, name='start_quiz'),  # Start a specific quiz
]