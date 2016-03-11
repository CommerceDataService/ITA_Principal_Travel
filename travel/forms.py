from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'
        # widgets = {
        #     'start_date': forms.DateField(required=True)
        # }
