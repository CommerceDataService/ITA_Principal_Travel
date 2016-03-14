from django.contrib import admin
from registration.models import RegistrationProfile
from registration.users import UsernameField
from django.utils.translation import ugettext_lazy as _
from .models import Event, Principal, Trip, Region, EventType, Agency, Office

class RegistrationReduxAdmin(admin.ModelAdmin):
    actions = ['activate_users']
    list_display = ('user','activated')
    raw_id_fields = ['user']
    search_fields = ('user__{0}'.format(UsernameField()),
                     'user__first_name', 'user__last_name')
    
    def activate_users(self, request, queryset):
        """
        Activates the selected users, if they are not already
        activated.
        """
        for profile in queryset:
            RegistrationProfile.objects.activate_user(profile.activation_key)

            profile.delete()

    activate_users.short_description = _("Activate users")

#unregister admin model and register it again to use new admin model
admin.site.unregister(RegistrationProfile)
admin.site.register(RegistrationProfile,RegistrationReduxAdmin)

admin.site.register(Event)
admin.site.register(Principal)
admin.site.register(Trip)
admin.site.register(Region)
admin.site.register(EventType)
admin.site.register(Agency)
admin.site.register(Office)


