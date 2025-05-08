# models.py
from django.db import models

class DeveloperProfile(models.Model):
    FRONTEND = 'Frontend'
    BACKEND = 'Backend'
    FULLSTACK = 'Fullstack'
    DATASCIENCE='Data science'
    MACHINELEARNING='Machine learning'
    CYBERSECURITY='Cyber security'

    EXPERTISE_CHOICES = [
        (FRONTEND, 'Frontend'),
        (BACKEND, 'Backend'),
        (FULLSTACK, 'Fullstack'),
        (DATASCIENCE, 'Datas cience'),
        (MACHINELEARNING, 'Machine learning'),
        (CYBERSECURITY, 'Cyber security'),
    ]

    user = models.CharField(max_length=555)
    expertise = models.CharField(
        max_length=100,
        choices=EXPERTISE_CHOICES,
        default=FRONTEND,
    )
    git_repo = models.URLField(max_length=555, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.expertise}"