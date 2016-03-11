from datetime import datetime, date, timedelta
from django import forms
from .models import Trip, Event, Principal

class TripForm(forms.ModelForm):
    start_date = forms.DateField(initial=date.today)
    end_date = forms.DateField(initial=date.today() + timedelta(days=5))
    class Meta:
        model = Trip
        fields = '__all__'
        # widgets = {
        #     'start_date': forms.DateField(required=True)
        # }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class PrincipalForm(forms.ModelForm):
    career = forms.CheckboxInput()
    class Meta:
        model = Principal
        fields = '__all__'
