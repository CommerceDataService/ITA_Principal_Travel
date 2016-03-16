from .models import Trip, Event, Principal
from .forms import TripForm, EventForm, PrincipalForm
from django.views.generic import ListView, DetailView, TemplateView
from django.template.loader import get_template
from django.shortcuts import render, redirect
from .serializers import TripSerializer, EventSerializer
from rest_framework import viewsets

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

def dashboard_view(request):
    return render(request, 'travel/dashboard.html')

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all();
    serializer_class = EventSerializer
