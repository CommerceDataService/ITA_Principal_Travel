import django_filters
from .models import Trip, Event, Region, EventType
from cities_light.models import Country

class TripFilter(django_filters.FilterSet):
    Principal_title = django_filters.CharFilter(lookup_expr='icontains', name='principal__title')
    Quick_Dates = django_filters.DateRangeFilter()
    Custom_Date_Range = django_filters.DateFromToRangeFilter()
    Month = django_filters.NumberFilter(name='start_date__month')
    Year = django_filters.NumberFilter(name='start_date__year')
    Region = django_filters.ModelChoiceFilter(queryset = Region.objects.all(), name='events__cities_light_country__custom_region')
    Country = django_filters.ModelChoiceFilter(queryset = Country.objects.all(), name='events__cities_light_country__name')
    Event_Type = django_filters.ModelChoiceFilter(queryset = EventType.objects.all(), name='events__event_type')

    class Meta:
        model = Trip
        fields = []
