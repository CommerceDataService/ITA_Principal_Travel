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
from django.conf.urls import url, include, patterns
from django.contrib import admin
from travel.views import TripViewSet
from travel.views import TripList
from travel.views import TripViewSet
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')), #Using simple urls now for one-step registration. Option below to be used for future use of two-step method
    # url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', 'travel.views.home', name='home'),
    url(r'^itinerary/$', TripList.as_view(), name='tripList') 
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
