from django.db import models
import uuid
from django.conf import settings  # Import settings to use the custom user model

class Referral(models.Model):
    referrer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='referrals', on_delete=models.CASCADE)
    invite_code = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.referrer.username} - {self.invite_code}"