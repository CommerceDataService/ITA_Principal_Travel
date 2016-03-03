from .models import EventLocationPrincipalTravel
from .serializers import ELPTSerializer
from rest_framework import viewsets
from django.views.generic import ListView
from django.views.generic import DetailView

# Create your views here.
class TripViewSet(viewsets.ModelViewSet):
    queryset = EventLocationPrincipalTravel.objects.all()
    serializer_class = ELPTSerializer

class EventLocationPrincipalTravelList(ListView):
    model = EventLocationPrincipalTravel

class EventLocationPrincipalTravelDetail(DetailView):
    queryset = EventLocationPrincipalTravel.objects.all()

    def get_object(self):
        object = super(EventLocationPrincipalTravelDetail, self).get_object()
        return object
