from django import forms
from .models import WithdrawalRequest

class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = WithdrawalRequest
        fields = ['amount']  # Only include amount since phone_number is filled from Account