from django import forms
from .models import MpesaTransaction

class MpesaTransactionForm(forms.ModelForm):
    class Meta:
        model = MpesaTransaction
        fields = ['phone_number', 'amount']