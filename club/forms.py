from django import forms
from .models import SportsFacility

class SportsFacilityForm(forms.ModelForm):
    class Meta:
        model = SportsFacility
        fields = '__all__'
