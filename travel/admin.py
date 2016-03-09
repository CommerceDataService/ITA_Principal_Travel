from django.contrib import admin

# Register your models here.

from .models import Event, Principal, Trip, Region, EventType, Agency, Office

admin.site.register(Event)
admin.site.register(Principal)
admin.site.register(Trip)
admin.site.register(Region)
admin.site.register(EventType)
admin.site.register(Agency)
admin.site.register(Office)
