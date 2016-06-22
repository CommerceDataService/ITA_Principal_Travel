from datetime import datetime, date, timedelta
from dal import autocomplete
from django import forms
from .models import Trip, Event, Principal
from cities_light.models import City
from datetimewidget.widgets import DateWidget

class TripForm(forms.ModelForm):
    events = forms.ModelMultipleChoiceField(
        queryset = Event.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='event-autocomplete')
    )
    start_date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    end_date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    class Meta:
        model = Trip
        fields = ('principal', 'start_date', 'end_date', 'events', 'no_of_travelers', 'no_of_travelers_note')
        help_texts = {
            'events': 'CTRL + click to select multiple events for this trip. (&#8984; + Click if using Mac OS)',
        }

class EventForm(forms.ModelForm):
    cities_light_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=autocomplete.ModelSelect2(url='city-autocomplete'),
        label="City"
    )
    class Meta:
        model = Event
        fields = ('name', 'description', 'event_type', 'cities_light_city', 'host', 'press', 'press_note')


class PrincipalForm(forms.ModelForm):
    career = forms.CheckboxInput()
    class Meta:
        model = Principal
        fields = ('first_name', 'last_name', 'title', 'office', 'region', 'career')
