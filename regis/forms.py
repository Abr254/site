from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
# forms.py

from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

CustomUser = get_user_model()  # This ensures you're using the custom user model

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    phone_number = forms.CharField(
        label='Phone Number',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be in a valid format.")]
    )

    class Meta:
        model = CustomUser  # Use the custom user model here
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    # Custom password fields to handle password confirmation
    


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')

