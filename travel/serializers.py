from .models import Trip, Event, Principal, EventType
from cities_light.models import Country, City, Region
from rest_framework import serializers

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ('id', 'name')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')

class CitySerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    class Meta:
        model = City
        fields = ('id', 'name', 'region', 'latitude', 'longitude')

class EventSerializer(serializers.ModelSerializer):
    cities_light_country = CountrySerializer(read_only=True)
    cities_light_city = CitySerializer(read_only=True)
    event_type = EventTypeSerializer(read_only=True)
    class Meta:
        model = Event
        fields = '__all__'

class PrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principal
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)
    principal = PrincipalSerializer(read_only=True)
    class Meta:
        model = Trip
        fields = '__all__'
