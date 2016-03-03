from .models import EventLocationPrincipalTravel
from .serializers import ELPTSerializer
from rest_framework import viewsets
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class TripViewSet(viewsets.ModelViewSet):
    queryset = EventLocationPrincipalTravel.objects.all()
    serializer_class = ELPTSerializer

class EventLocationPrincipalTravelList(ListView):
    model = EventLocationPrincipalTravel

class EventLocationPrincipalTravelDetail(DetailView):
    model = EventLocationPrincipalTravel

    def get_context_data(self, **kwargs):
        context = super(EventLocationPrincipalTravelDetail, self).get_context_data(**kwargs)
        return context
