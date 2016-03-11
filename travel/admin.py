from django.contrib import admin
#from registration.models import RegistrationManager

# Register your models here.

from .models import Event, Principal, Trip, Region, EventType, Agency, Office

#def make_active(modeladmin, request, queryset):
#    queryset.update(activated= true)
#make_published.short_description = "Activate selected users"

#class RegistrationActivation(admin.ModelAdmin):
#    list_display = ['username', 'status']
#    ordering = ['username']
#    actions = [make_active]

admin.site.register(Event)
admin.site.register(Principal)
admin.site.register(Trip)
admin.site.register(Region)
admin.site.register(EventType)
admin.site.register(Agency)
admin.site.register(Office)
#admin.site.register(RegistrationManager)
#admin.site.register(RegistrationProfile,RegistrationActivation)


