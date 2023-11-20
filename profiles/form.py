# profiles/forms.py
from django import forms
from .models import Profile

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['lon', 'lat']  # Add other fields as needed
