# chat/models.py

from django.conf import settings  # Import settings to refer to the custom user model
from django.db import models

class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Correctly references custom user model
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when the message is created

    def __str__(self):
        return f'{self.user.username}: {self.text[:20]}'