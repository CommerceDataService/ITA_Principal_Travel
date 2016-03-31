from datetime import datetime, date, timedelta
from dal import autocomplete
from django import forms
from .models import Trip, Event, Principal
from cities_light.models import City


class TripForm(forms.ModelForm):
    start_date = forms.DateField(initial=date.today)
    end_date = forms.DateField(initial=date.today() + timedelta(days=5))
    class Meta:
        model = Trip
        fields = ('principal', 'start_date', 'end_date', 'events', 'no_of_travelers', 'no_of_travelers_note')
        help_texts = {
            'events': 'CTRL + click to select multiple events for this trip. (&#8984; + Click if using Mac OS)',
        }

class EventForm(forms.ModelForm):
    cities_light_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=autocomplete.ModelSelect2(url='city-autocomplete')
    )
    class Meta:
        model = Event
        fields = ('name', 'description', 'event_type', 'cities_light_city', 'host', 'press', 'press_note')


class PrincipalForm(forms.ModelForm):
    career = forms.CheckboxInput()
    class Meta:
        model = Principal
        fields = ('first_name', 'last_name', 'title', 'office', 'region', 'career')
