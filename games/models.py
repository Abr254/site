from django.db import models
from django.conf import settings

class Earnings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    site = models.CharField(max_length=255, blank=True, null=True)  # Site where earnings came from
    quiz = models.CharField(max_length=255, blank=True, null=True)  # Optional quiz info
    score = models.IntegerField(blank=True, null=True)  # Optional score
    earned = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.earned} on {self.created_at.date()} from {self.site or 'Unknown'}"