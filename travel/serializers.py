from .models import Event, Location, Principal, Travel, EventLocationPrincipalTravel
from rest_framework import serializers

class ELPTSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.StringRelatedField()
    location = serializers.StringRelatedField()
    principal = serializers.StringRelatedField()
    travel = serializers.StringRelatedField()

    class Meta:
        model = EventLocationPrincipalTravel
        fields = ('event', 'location', 'principal', 'travel')
