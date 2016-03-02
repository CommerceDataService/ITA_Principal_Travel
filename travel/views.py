from .models import EventLocationPrincipalTravel
from .serializers import ELPTSerializer
from rest_framework import viewsets
from django.shortcuts import render

# Create your views here.
class TripViewSet(viewsets.ModelViewSet):
    queryset = EventLocationPrincipalTravel.objects.all()
    serializer_class = ELPTSerializer

def home(request):
    return render(request, 'home.html')
