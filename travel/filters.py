import django_filters
from .models import Trip, Event, Region, EventType
from cities_light.models import Country
from datetimewidget.widgets import DateWidget

class TripFilter(django_filters.FilterSet):
    principal_title = django_filters.CharFilter(lookup_expr='icontains', name='principal__title')
    quick_dates = django_filters.DateRangeFilter()
    custom_date_range = django_filters.DateFromToRangeFilter(widget=DateWidget(usel10n=True, bootstrap_version=3))
    month = django_filters.NumberFilter(name='start_date__month')
    year = django_filters.NumberFilter(name='start_date__year')
    region = django_filters.ModelChoiceFilter(queryset = Region.objects.all(), name='events__cities_light_country__custom_region')
    country = django_filters.ModelChoiceFilter(queryset = Country.objects.all(), name='events__cities_light_country__name')
    event_type = django_filters.ModelChoiceFilter(queryset = EventType.objects.all(), name='events__event_type')

    class Meta:
        model = Trip
        fields = []
