from django.db import models
from django.conf import settings  # This points to the custom user model
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # <-- Add this for multi-line input
    reward_per_question = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

        
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()  # Changed from CharField to TextField
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)

    def __str__(self):
        return self.question_text

class QuizAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    earned = models.FloatField()
    attempted_at = models.DateTimeField(auto_now_add=True)

@receiver(pre_save, sender=Quiz)
def set_reward_per_question(sender, instance, **kwargs):
    if instance.reward_per_question is None:
        num_questions = instance.question_set.count()
        if num_questions > 0:
            instance.reward_per_question = 80.0 / num_questions