from django import forms
from .models import Transport

class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ['name', 'vehicle_type', 'registration_number', 'capacity', 'description']
