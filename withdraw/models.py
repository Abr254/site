from django.db import models
from django.contrib.auth import get_user_model
from django.contrib import admin
#from .models import WithdrawalRequest

#admin.site.register(WithdrawalRequest)
User = get_user_model()

class WithdrawalRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # <-- add this line

    def __str__(self):
        return f"{self.user.username} - Ksh{self.amount} - {self.status}"