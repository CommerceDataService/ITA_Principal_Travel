from travel.models import Trip, Event, Principal
from travel.forms import TripForm, EventForm, PrincipalForm
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q, Count, Func, F, Value
from travel.serializers import TripSerializer, EventSerializer
from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from dal import autocomplete
from cities_light.models import City, Country
from .mixins import FilterMixin
from .filters import TripFilter
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import date
from django.http import HttpResponse
import calendar
import datetime


class LoginRequiredView(LoginRequiredMixin):
    login_url = '/accounts/login/'


class HealthCheckView(TemplateView):
    ''' This is primarily for the ELB to be able to check that the instance is
        still up. We need a separate URL to let ELB bypass HTTP Auth, or else it
        will stop routing traffic to our instance.
    '''
    template_name = 'health.html'


class HomeView(TemplateView):
    template_name = 'travel/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class TripDetail(LoginRequiredView, DetailView):
    queryset = Trip.objects.all()

    def get_object(self):
        object = super(TripDetail, self).get_object()
        return object


class TripList(LoginRequiredView, FilterMixin, ListView):
    model = Trip
    filter_class = TripFilter
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = super(TripList, self).get_queryset(*args, **kwargs)
        return qs

    def get_context_data(self,**kwargs):
        context = super(TripList, self).get_context_data(**kwargs)
        page_query_dict = self.request.GET
        page_URL = self.request.get_full_path()
        page_URL_length = len(page_URL)

        if page_URL_length > 13 :

            month = page_query_dict['month']
            region = page_query_dict['region']
            principal_title = page_query_dict['principal_title']
            date_range_end = page_query_dict['date_range_end']
            date_range_start = page_query_dict['date_range_start']
            country_ID = page_query_dict['country']
            country_ID_2 = len(country_ID)
            principal_name = page_query_dict['principal_name']
            event_type = page_query_dict['event_type']
            year = page_query_dict['year']
            quick_dates = page_query_dict['quick_dates']
            event_name = page_query_dict['event_name']
            event_description = page_query_dict['event_description']

            context['event_name'] = event_name
            context['event_description'] = event_description
            context['date_range_start'] = date_range_start
            context['date_range_end'] = date_range_end
            context['month'] = month
            context['region'] = region
            context['principal_title'] = principal_title
            context['principal_name'] = principal_name
            context['event_type'] = event_type
            context['year'] = year
            context['quick_dates'] = quick_dates

            if country_ID_2 > 0 :
                country = Country.objects.get(id=country_ID)
                context['country'] = country
            else :
                context['country'] = country_ID

        return context


@login_required(login_url='/accounts/login/')
def trip_new(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.save()
            form.save_m2m()
            messages.success(request, 'A new itinerary was successfully created.')
            return redirect('trip_detail', pk=trip.pk)
    else:
        form = TripForm()
    return render(request, 'travel/trip_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def trip_edit(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.save()
            form.save_m2m()
            messages.success(request, 'The itinerary was successfully updated.')
            return redirect('trip_detail', pk=trip.pk)
    else:
        form = TripForm(instance=trip)
    return render(request, 'travel/trip_form.html', {'form': form, 'trip': trip})


@login_required(login_url='/accounts/login/')
def trip_delete(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        trip.delete()
        messages.success(request, 'The itinerary was successfully deleted.')
        return redirect('trip_list')
    return render(request, 'travel/trip_confirm_delete.html', {'trip': trip})


class EventList(LoginRequiredView, ListView):
    model = Event
    paginate_by = 10


class EventDetail(LoginRequiredView, DetailView):
    queryset = Event.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        context['trips'] = Trip.objects.filter(events__id=self.object.id)
        return context


@login_required(login_url='/accounts/login/')
def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.cities_light_country = event.cities_light_city.country
            event.save()
            form.save_m2m()
            messages.success(request, 'A new event was successfully created.')
            return redirect('trip_new')
    else:
        form = EventForm()
    return render(request, 'travel/event_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            form.save_m2m()
            messages.success(request, 'The event was successfully updated.')
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'travel/event_form.html', {'form': form, 'event': event})


class PrincipalList(LoginRequiredView, ListView):
    model = Principal
    paginate_by = 10


class PrincipalDetail(LoginRequiredView, DetailView):
    queryset = Principal.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PrincipalDetail, self).get_context_data(**kwargs)
        context['trips'] = Trip.objects.filter(principal__id=self.object.id)
        return context


@login_required(login_url='/accounts/login/')
def principal_new(request):
    if request.method == "POST":
        form = PrincipalForm(request.POST)
        if form.is_valid():
            principal = form.save(commit=False)
            principal.save()
            form.save_m2m()
            messages.success(request, 'A new principal record was successfully created.')
            return redirect('trip_new')
    else:
        form = PrincipalForm()
    return render(request, 'travel/principal_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def principal_edit(request, pk):
    principal = get_object_or_404(Principal, pk=pk)
    if request.method == "POST":
        form = PrincipalForm(request.POST, instance=principal)
        if form.is_valid():
            principal = form.save(commit=False)
            principal.save()
            form.save_m2m()
            messages.success(request, 'The principal record was successfully updated.')
            return redirect('principal_detail', pk=principal.pk)
    else:
        form = PrincipalForm(instance=principal)
    return render(request, 'travel/principal_form.html', {'form': form, 'principal': principal})


@login_required(login_url='/accounts/login/')
def dashboard_view(request):
    return render(request, 'travel/dashboard.html')


class TripViewSet(LoginRequiredView, viewsets.ModelViewSet):
    serializer_class = TripSerializer
    def get_queryset(self):
        queryset = Trip.objects.all()
        destination = self.request.query_params.get('destination', None)
        if destination is not None:
            if destination == "international":
                queryset = queryset.exclude(events__cities_light_country__id=234)
            elif destination == "domestic":
                queryset = queryset.filter(events__cities_light_country__id=234)
        return queryset



class EventViewSet(LoginRequiredView, viewsets.ModelViewSet):
    serializer_class = EventSerializer
    def get_queryset(self):
        queryset = Event.objects.all()
        destination = self.request.query_params.get('destination', None)
        if destination is not None:
            if destination == "international":
                queryset = queryset.exclude(cities_light_country__id=234)
            elif destination == "domestic":
                queryset = queryset.filter(cities_light_country__id=234)
        return queryset


class CityAutocomplete(LoginRequiredView, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = City.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

class EventNameAutocomplete(LoginRequiredView, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Event.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

class ReportView(LoginRequiredView, TemplateView):
    template_name = 'travel/report.html'

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        current_year = self.request.GET.get('year', date.today().year)
        report_type = self.request.GET.get('by', 'country')
        # Generating lists for template use
        unique_reporting_years = []
        years = Trip.objects.dates('start_date', 'year')
        for year in years:
            unique_reporting_years.append(year.strftime('%Y'))
        month_names = []
        for i in range(1, 13):
            month_names.append([i, calendar.month_name[i]])
        # Generating reports
        countries = None
        eventtypes = None
        regions = None
        principals = None
        if report_type == 'country':
            countries = Trip.objects.filter(start_date__year=current_year) \
                .values_list(
                    'events__cities_light_country__name',
                    'events__cities_light_country__id'
                ).distinct()
        elif report_type == 'event':
            eventtypes = Trip.objects.filter(start_date__year=current_year) \
                .values_list(
                    'events__event_type__name',
                    'events__event_type__id'
                ).distinct()
        elif report_type == 'region':
            regions = Trip.objects.filter(start_date__year=current_year) \
                .values_list(
                    'events__cities_light_country__agency_region__name',
                    'events__cities_light_country__agency_region__id'
                ).distinct()
            print(regions)
            print(regions.query)
        elif report_type == 'principal':
            principals = Trip.objects.filter(start_date__year=current_year).values_list('principal__last_name', 'principal__id').distinct()

        if countries:
            context['attributes'] = list(countries)
            context['query_string'] = 'country'
            country_names = [x[0] for x in countries]
            resultset = _report_queryset_by_attr(
                current_year=current_year,
                attr_set=country_names,
                orig_name='events__cities_light_country__name',
                orig_id='events__cities_light_country__id',
                new_name='country_name',
                new_id='country_id'
            )
            data = _munge_data(resultset, 'country_name')

        elif eventtypes:
            context['attributes'] = list(eventtypes)
            context['query_string'] = 'event_type'
            resultset = _report_queryset_by_attr(
                current_year=current_year,
                attr_set=[x[0] for x in eventtypes],
                orig_name='events__event_type__name',
                orig_id='events__event_type__id',
                new_name='event_type_name',
                new_id='event_type_id'
            )
            data = _munge_data(resultset, 'event_type_name')

        elif principals:
            context['attributes'] = list(principals)
            context['query_string'] = 'principal'
            resultset = _report_queryset_by_attr(
            current_year=current_year,
            attr_set=[x[0] for x in principals],
            orig_name='principal__last_name',
            orig_id='principal__id',
            new_name='principal_name',
            new_id='principal_id'
            )
            data = _munge_data(resultset, 'principal_name')

        elif regions:
            context['attributes'] = list(regions)
            context['query_string'] = 'region'
            queryset = Trip.objects.filter(Q(start_date__year=current_year)
                & (
                    Q(events__cities_light_country__agency_region__name__in=[x[0] for x in regions])
                    | Q(events__cities_light_country__agency_region__isnull=True)
                   )
            )
            resultset = _group_by_and_count(
                queryset=queryset,
                orig_name='events__cities_light_country__agency_region__name',
                orig_id='events__cities_light_country__agency_region__id',
                new_name='region_name',
                new_id='region_id'
            )
            data = _munge_data(resultset, 'region_name')


        context['year'] = current_year
        context['data_list'] = data
        context['months'] = month_names
        context['annual_report_list'] = unique_reporting_years
        context['report_type_list'] = ['country', 'region', 'event', 'principal']
        return context

def _report_queryset_by_attr(*args, **kwargs):
    queryset = _base_queryset_filters(*args, **kwargs)
    return _group_by_and_count(queryset, *args, **kwargs)

def _group_by_and_count(queryset, *args, **kwargs):
    return queryset \
        .annotate(month=Func(Value('month'), F('start_date'), function='date_part', template='%(function)s(%(expressions)s)::int')) \
        .values('month', kwargs['orig_name'], kwargs['orig_id']) \
        .annotate(**{'count': Count('*'), kwargs['new_name']: F(kwargs['orig_name']), kwargs['new_id']: F(kwargs['orig_id'])}) \
        .values('month', 'count', kwargs['new_id'], kwargs['new_name']) \
        .order_by(kwargs['new_id'], 'month')

def _base_queryset_filters(*args, **kwargs):
    return Trip.objects \
        .filter(Q(start_date__year=kwargs.get('current_year', 2016)) & Q(**{kwargs['orig_name'] + '__in': kwargs['attr_set']})) \

def _munge_data(resultset, attr_y):
    data = {}
    for r in resultset:
        if not data.get(r[attr_y]):
            data[r[attr_y]] = {}
        if not data[r[attr_y]].get(r['month']):
            data[r[attr_y]][r['month']] = {}
        data[r[attr_y]][r['month']] = r['count']
    return data
