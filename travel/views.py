from .models import Trip, Event, Principal
from .forms import TripForm, EventForm, PrincipalForm
from django.views.generic import ListView, DetailView, TemplateView
from django.template.loader import get_template
from django.shortcuts import render, redirect, get_object_or_404
from dal import autocomplete
from cities_light.models import Country, City

# Create your views here.
class HomeView(TemplateView):
    template_name = 'travel/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

class TripDetail(DetailView):
    queryset = Trip.objects.all()

    def get_object(self):
        object = super(TripDetail, self).get_object()
        return object

class TripList(ListView):
	model = Trip

def trip_new(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        trip = form.save(commit=False)
        trip.save()
        form.save_m2m()
        return redirect('trip_detail', pk=trip.pk)
    else:
        form = TripForm()
    return render(request, 'travel/trip_form.html', {'form': form})

def trip_edit(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        form = TripForm(request.POST, instance=trip)
        trip = form.save(commit=False)
        trip.save()
        form.save_m2m()
        return redirect('trip_detail', pk=trip.pk)
    else:
        form = TripForm(instance=trip)
    return render(request, 'travel/trip_form.html', {'form': form})

def trip_delete(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        trip.delete()
        return redirect('trip_list')
    return render(request, 'travel/trip_confirm_delete.html', {'trip': trip})

class EventList(ListView):
    model = Event

class EventDetail(DetailView):
    queryset = Event.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        context['trips'] = Trip.objects.filter(events__id = self.object.id)
        return context

def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        event = form.save(commit=False)
        event.save()
        form.save_m2m()
        return redirect('trip_new')
    else:
        form = EventForm()
    return render(request, 'travel/event_form.html', {'form': form})

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        event = form.save(commit=False)
        event.save()
        form.save_m2m()
        return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'travel/event_form.html', {'form': form})

def principal_new(request):
    if request.method == "POST":
        form = PrincipalForm(request.POST)
        principal = form.save(commit=False)
        principal.save()
        form.save_m2m()
        return redirect('trip_new')
    else:
        form = PrincipalForm()
    return render(request, 'travel/principal_form.html', {'form': form})


class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return City.objects.none()

        qs = City.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
