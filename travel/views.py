from .models import EventLocationPrincipalTravel
from restless.views import Endpoint
from restless.models import serialize

# Create your views here.
class TripList(Endpoint):
    def get(self, request):
        all = EventLocationPrincipalTravel.objects.all()
        return serialize(all)


