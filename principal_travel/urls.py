"""principal_travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from travel.views import HomeView, TripDetail, TripList, trip_new, event_new, \
    principal_new, trip_edit, trip_delete, event_edit, EventList, \
    EventDetail, dashboard_view, TripViewSet, EventViewSet, \
    CityAutocomplete, PrincipalList, PrincipalDetail, principal_edit, \
    ReportView, HealthCheckView, EventNameAutocomplete
from rest_framework import routers
from django.contrib.staticfiles import views


router = routers.DefaultRouter()
router.register(r'trips', TripViewSet, base_name='Trip')
router.register(r'events', EventViewSet, base_name='Event')

urlpatterns = [
    # url(r'^search/$', search, name='search'),
    url(r'^$', HomeView.as_view(), name='home_view'),
    url(r'^health/', HealthCheckView.as_view(), name='health_view'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    # url(r'^accounts/', include('registration.backends.simple.urls')), #Using simple urls now for one-step registration. Option below to be used for future use of two-step method
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^itineraries/$', TripList.as_view(), name='trip_list'),
    url(r'^itineraries/(?P<pk>[0-9]+)/$', TripDetail.as_view(), name='trip_detail'),
    url(r'^itineraries/new/$', trip_new, name="trip_new"),
    url(r'^itineraries/(?P<pk>[0-9]+)/edit/$', trip_edit, name="trip_edit"),
    url(r'^itineraries/(?P<pk>[0-9]+)/delete/$', trip_delete, name="trip_delete"),
    url(r'^events/$', EventList.as_view(), name='event_list'),
    url(r'^events/(?P<pk>[0-9]+)/$', EventDetail.as_view(), name='event_detail'),
    url(r'^events/new/$', event_new, name="event_new"),
    url(r'^events/(?P<pk>[0-9]+)/edit/$', event_edit, name="event_edit"),
    url(r'^principals/$', PrincipalList.as_view(), name='principal_list'),
    url(r'^principals/(?P<pk>[0-9]+)/$', PrincipalDetail.as_view(), name='principal_detail'),
    url(r'^principals/new/$', principal_new, name="principal_new"),
    url(r'^principals/(?P<pk>[0-9]+)/edit/$', principal_edit, name="principal_edit"),
    url(r'^dashboard$', dashboard_view, name='dashboard'),
    url(r'^city-autocomplete/$', CityAutocomplete.as_view(), name='city-autocomplete'),
    url(r'^event-autocomplete/$', EventNameAutocomplete.as_view(), name='event-autocomplete'),
    url(r'^report/$', ReportView.as_view(), name='report')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^static/(?P<path>.*)$', views.serve),
    ]
