import django_filters
from .models import Trip, Event

class TripFilter(django_filters.FilterSet):
    start_date = django_filters.DateFromToRangeFilter()
    events = django_filters.ModelMultipleChoiceFilter(name ='events__name', to_field_name='name', lookup_type='in', queryset = Event.objects.all())

    # event_type = django_filters.ModelMultipleChoiceFilter(name ='events__event_type__name', to_field_name='event_type__name', lookup_type='in', queryset = Event.objects.all())

    class Meta:
        model = Trip
        fields = {
        'principal__title': ['icontains'],
        }
