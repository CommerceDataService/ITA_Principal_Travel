from .models import EventLocationPrincipalTravel
from .serializers import ELPTSerializer
from rest_framework import viewsets
from django.shortcuts import render

# Create your views here.
class TripViewSet(viewsets.ModelViewSet):
    queryset = EventLocationPrincipalTravel.objects.all()
    serializer_class = ELPTSerializer

def home(request):
    print(request.user)
<<<<<<< HEAD
    return render(request, 'home.html', {'current_user': request.user})
=======
    return render(request, 'travel/home.html', {'current_user': request.user})
>>>>>>> 69bccf2ddb981810766de3356e61ecc2b44345b0
