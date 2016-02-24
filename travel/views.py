from .models import EventLocationPrincipalTravel
from .serializers import ELPTSerializer
from rest_framework import viewsets

# Create your views here.
class TripViewSet(viewsets.ModelViewSet):
    queryset = EventLocationPrincipalTravel.objects.all()
    serializer_class = ELPTSerializer
