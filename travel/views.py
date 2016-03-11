from .models import Trip
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.template.loader import get_template
from django.shortcuts import render

# Create your views here.
class TripDetail(DetailView):
    queryset = Trip.objects.all()

    def get_object(self):
        object = super(TripDetail, self).get_object()
        return object

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

def home(request):
    print(request.user)
    return render(request, 'travel/home.html', {'current_user': request.user})

class TripList(ListView):
	model = Trip
