from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

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
        model = CustomUser
        fields = ['username', 'phone_number']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])  # Hash the password
        user.phone_number = self.cleaned_data['phone_number']  # Save phone number
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')