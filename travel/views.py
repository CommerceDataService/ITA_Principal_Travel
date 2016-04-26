from .models import Trip, Event, Principal
from .forms import TripForm, EventForm, PrincipalForm
from django.views.generic import ListView, DetailView, TemplateView
from .serializers import TripSerializer, EventSerializer
from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from dal import autocomplete
from cities_light.models import City
from .mixins import FilterMixin
from .filters import TripFilter
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import date
import calendar


class LoginRequiredView(LoginRequiredMixin):
    login_url = '/accounts/login/'


class HealthCheckView(TemplateView):
    ''' This is primarily for the ELB to be able to check that the instance is still up.
        We need a separate URL to let ELB bypass HTTP Auth, or else it will stop routing
        traffic to our instance.
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
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class EventViewSet(LoginRequiredView, viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CityAutocomplete(LoginRequiredView, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return City.objects.none()

        qs = City.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class ReportView(LoginRequiredView, TemplateView):
    template_name = 'travel/report.html'

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        current_year = self.request.GET.get('year')
        report_type = self.request.GET.get('by')
        if current_year is None:
            current_year = (date.today()).year
        if report_type is None:
            report_type = 'country'
        # Generating lists for template use
        unique_reporting_years = []
        years = Trip.objects.dates('start_date', 'year')
        for year in years:
            unique_reporting_years.append(year.strftime('%Y'))
        month_names = []
        for i in range(1, 13):
            month_names.append([i, calendar.month_name[i]])
        # Generating reports
        data = []
        countries = None
        eventtypes = None
        regions = None
        if report_type == 'country':
            countries = Trip.objects.filter(start_date__year=current_year). values_list('events__cities_light_country__name', 'events__cities_light_country__id').distinct()
        elif report_type == 'event':
            eventtypes = Trip.objects.filter(start_date__year=current_year).values_list('events__event_type__name', 'events__event_type__id').distinct()
        elif report_type == 'region':
            regions = Trip.objects.filter(start_date__year=current_year).values_list('events__cities_light_country__custom_region__name', 'events__cities_light_country__custom_region__id').distinct()
            print(regions)

        months = Trip.objects.filter(start_date__year=current_year).dates('start_date', 'month')
        for month in months:
            month = month.strftime('%m')
            if countries:
                context['attributes'] = countries
                context['query_string'] = 'country'
                for country in countries:
                    trip_count = Trip.objects.filter(start_date__year=current_year).filter(start_date__month=month).filter(events__cities_light_country__name=country[0]).count()
                    data.append({'month': month[1], 'attribute_name': country[0], 'attribute_id': country[1], 'count': trip_count})
            elif eventtypes:
                context['attributes'] = eventtypes
                context['query_string'] = 'event_type'
                for eventtype in eventtypes:
                    trip_count = Trip.objects.filter(start_date__year=current_year).filter(start_date__month=month).filter(events__event_type__name=eventtype[0]).count()
                    data.append({'month': month[1], 'attribute_name': eventtype[0], 'attribute_id': eventtype[1], 'count': trip_count})
            elif regions:
                context['attributes'] = regions
                context['query_string'] = 'region'
                for region in regions:
                    trip_count = Trip.objects.filter(start_date__year=current_year).filter(start_date__month=month).filter(events__cities_light_country__custom_region__name=region[0]).count()
                    data.append({'month': month[1], 'attribute_name': region[0], 'attribute_id': region[1], 'count': trip_count})

        context['year'] = current_year
        context['data_list'] = data
        context['months'] = month_names
        context['annual_report_list'] = unique_reporting_years
        context['report_type_list'] = ['country', 'region', 'event']
        return context
