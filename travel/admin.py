from django.contrib import admin

# Register your models here.

from .models import Event, EventLocPrincipalTravel, EventLocation, Location, Principal, PrincipalTravel, Travel

admin.site.register(Event)
admin.site.register(EventLocPrincipalTravel)
admin.site.register(EventLocation)
admin.site.register(Location)
admin.site.register(Principal)
admin.site.register(PrincipalTravel)
admin.site.register(Travel)
