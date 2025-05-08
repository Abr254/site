# forms.py
from django import forms
from .models import DeveloperProfile

class DeveloperProfileForm(forms.ModelForm):
    class Meta:
        model = DeveloperProfile
        fields = ['user', 'expertise', 'git_repo', 'description']