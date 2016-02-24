from django.contrib import admin

# Register your models here.

from .models import Event, Location, Principal, Travel, EventLocationPrincipalTravel

admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Principal)
admin.site.register(Travel)
admin.site.register(EventLocationPrincipalTravel)
