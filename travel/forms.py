from datetime import datetime, date, timedelta
from django import forms
from .models import Trip, Event, Principal

class TripForm(forms.ModelForm):
    start_date = forms.DateField(initial=date.today)
    end_date = forms.DateField(initial=date.today() + timedelta(days=5))
    class Meta:
        model = Trip
        fields = ('principal', 'start_date', 'end_date', 'events', 'no_of_travelers', 'no_of_travelers_note')

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'description', 'event_type', 'cities_light_country', 'cities_light_city', 'host', 'press', 'press_note')

class PrincipalForm(forms.ModelForm):
    career = forms.CheckboxInput()
    class Meta:
        model = Principal
        fields = ('first_name', 'last_name', 'title', 'office', 'region', 'career')
