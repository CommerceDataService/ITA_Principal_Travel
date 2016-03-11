from .models import EventLocationPrincipalTravel
from .models import Trip
from django.views.generic import ListView
from .serializers import ELPTSerializer
from rest_framework import viewsets
from .models import EventLocationPrincipalTravel
from .serializers import ELPTSerializer
from rest_framework import viewsets
from django.shortcuts import render

def home(request):
    print(request.user)
    return render(request, 'travel/home.html', {'current_user': request.user})

class TripList(ListView):
	model = Trip
