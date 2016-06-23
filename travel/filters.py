import django_filters
from .models import Trip, Event, Region, EventType, Principal
from cities_light.models import Country
from datetimewidget.widgets import DateWidget

class TripFilter(django_filters.FilterSet):
    principal_title = django_filters.CharFilter(lookup_expr='icontains', name='principal__title', label='Principal Title')
    principal_name = django_filters.CharFilter(lookup_expr='icontains', name='principal__last_name', label='Principal Lastname')
    principal =django_filters.ModelChoiceFilter(queryset = Principal.objects.all(), name='principal')
    quick_dates = django_filters.DateRangeFilter(label='Quick Dates', name='start_date')
    date_range_start = django_filters.DateFilter(lookup_expr='gte', name='start_date', widget=DateWidget(usel10n=True, bootstrap_version=3), label='Custom Date Range - From')
    date_range_end = django_filters.DateFilter(lookup_expr='lte', name='start_date', widget=DateWidget(usel10n=True, bootstrap_version=3), label='Custom Date Range - To')
    month = django_filters.NumberFilter(name='start_date__month', help_text='Enter numeric value for month(e.g. 1 for January)')
    year = django_filters.NumberFilter(name='start_date__year')
    region = django_filters.ModelChoiceFilter(queryset = Region.objects.all(), name='events__cities_light_country__agency_region')
    country = django_filters.ModelChoiceFilter(queryset = Country.objects.all(), name='events__cities_light_country__name')
    event_type = django_filters.ModelChoiceFilter(queryset = EventType.objects.all(), name='events__event_type', label='Event Type')
    event_name = django_filters.CharFilter(lookup_expr='icontains', name='events__name', label='Event Name')
    event_description = django_filters.CharFilter(lookup_expr='icontains', name='events__description', label='Event Description')

    class Meta:
        model = Trip
        fields = []
