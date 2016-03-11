from .models import EventLocationPrincipalTravel
from .models import Trip
from django.views.generic import ListView
from .serializers import ELPTSerializer
from rest_framework import viewsets
from django.shortcuts import render

# Create your views here.
class TripViewSet(viewsets.ModelViewSet):
    queryset = EventLocationPrincipalTravel.objects.all()
    serializer_class = ELPTSerializer

def home(request):
    print(request.user)
    return render(request, 'travel/home.html', {'current_user': request.user})

class TripList(ListView):
	model = Trip