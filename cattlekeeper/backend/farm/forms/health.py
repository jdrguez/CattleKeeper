from django import forms
from ..models.health import HealthEvent

class HealthEventForm(forms.ModelForm):
    class Meta:
        model = HealthEvent
        fields = ['date', 'event_type', 'description']
