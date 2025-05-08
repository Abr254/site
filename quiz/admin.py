from django import forms
from django.contrib import admin
from .models import Quiz, Question, QuizAttempt

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 5,
                'cols': 80,
                'style': 'white-space: pre-wrap;'  # Preserve line breaks
            }),
        }


class QuestionInlineForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'question_text': forms.Textarea(attrs={
                'rows': 3,
                'cols': 60,
                'style': 'white-space: pre-wrap;'
            }),
        }

class QuestionTabularInline(admin.TabularInline):
    model = Question
    form = QuestionInlineForm
    extra = 5

class QuizAdmin(admin.ModelAdmin):
    form = QuizForm
    list_display = ('title', 'category', 'reward_per_question', 'created_at')
    inlines = [QuestionTabularInline]

class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'earned', 'attempted_at')
    list_filter = ('quiz', 'user')

admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizAttempt, QuizAttemptAdmin)