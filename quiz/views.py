from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Quiz, QuizAttempt
from regis.models import Account  # Import Account model instead of Profile

# View for listing all quizzes
def quiz_list(request):
    quizzes = Quiz.objects.all()  # Get all quizzes from the database
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

# View for starting a specific quiz
def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)  # Fetch quiz by ID or return 404 if not found
    questions = quiz.question_set.all()

    if request.method == 'POST':
        score = 0
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected == question.correct_option:
                score += 1

        earned = Decimal(score) * Decimal(quiz.reward_per_question)  # Convert earned to Decimal

        # Add to Account balance
        account, created = Account.objects.get_or_create(user=request.user)
        account.balance += earned  # No more type mismatch
        account.save()

        QuizAttempt.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            earned=earned
        )

        messages.success(request, f'You earned Ksh {earned:.2f}')
        return redirect('quiz_list')

    return render(request, 'start_quiz.html', {'quiz': quiz, 'questions': questions})