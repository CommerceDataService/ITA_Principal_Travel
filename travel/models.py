# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from cities_light.models import City,Country


class Event(models.Model):
    '''
    id = models.AutoField(primary_key=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    event_description = models.TextField(blank=True, null=True)
    iga_leg = models.CharField(max_length=10, blank=True, null=True)
    press = models.NullBooleanField()
    press_note = models.CharField(max_length=255, blank=True, null=True)
    no_of_travelers = models.IntegerField(blank=True, null=True)
    no_of_travelers_note = models.CharField(max_length=32, blank=True, null=True)
    '''

    id = models.AutoField(primary_key=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    event_name = models.CharField(max_length=255,blank=True, null=True)
    event_description = models.TextField(blank=True, null=True)
    event_type_id = models.ForeignKey('EventType',null=True)
    press = models.NullBooleanField()
    press_note = models.CharField(max_length=255, blank=True, null=True)

    no_of_travelers = models.IntegerField(blank=True, null=True)
    no_of_travelers_note = models.CharField(max_length=32, blank=True, null=True)

    cities_light_city = models.ForeignKey('cities_light.City',null=True)
    cities_light_country = models.ForeignKey('cities_light.Country',null=True)

    def __str__(self):
        return "{}".format(self.event_name)

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{}, {}, {}".format(self.city, self.state, self.country)

class Principal(models.Model):
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    agency = models.CharField(max_length=255, blank=True, null=True)
    principal_poc = models.CharField(max_length=255, blank=True, null=True)
    '''
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255, blank=True, null=True)

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    
    agency = models.CharField(max_length=255, blank=True, null=True)

    agency_id  = models.ForeignKey('Agency', null=True)
    career = models.BooleanField(default=False)
    region = models.ForeignKey('Region', null=True)

    def __str__(self):
        return "{}, {}, {}".format(self.first_name, self.last_name, self.title)

class Travel(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=32, blank=True, null=True)
    format = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return "{}, {}, {}".format(self.start_date, self.end_date, self.format)

class EventLocationPrincipalTravel(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey('Event', null=True)
    location = models.ForeignKey('Location', null=True)
    principal = models.ForeignKey('Principal', null=True)
    travel = models.ForeignKey('Travel', null=True)

    def __str__(self):
        return "{} {} {} {}".format(self.event, self.location, self.principal, self.travel)

class Trip(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    no_of_travelers = models.IntegerField(blank=True, null=True)
    no_of_travelers_note = models.CharField(max_length=32, blank=True, null=True)
    principal = models.ForeignKey('Principal', null=False)

    def __str__(self):
        return "{}, {}, {}".format(self.start_date, self.end_date)

class TripEvent(models.Model):
    id = models.AutoField(primary_key=True)
    trip = models.ForeignKey('Trip', null=False)
    event = models.ForeignKey('Event', null=False)

    def __str__(self):
        return "{}, {}".format(self.trip, self.event)

class Region(models.Model):
    id = models.AutoField(primary_key=True)
    region_name = models.CharField(max_length=255, blank=False, null=False)
    agency = models.ForeignKey('Agency', null=True)

    def __str__(self):
        return "{}".format(self.region_name)

class EventType(models.Model):
    id = models.AutoField(primary_key=True)
    event_type_name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return "{}".format(self.event_type_name)

class Agency(models.Model):
    id = models.AutoField(primary_key=True)
    agency_name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{}".format(self.agency_name)

class Office(models.Model):
    id = models.AutoField(primary_key=True)
    office_name = models.CharField(max_length=255, null=True)
    agency = models.ForeignKey('Agency', null=True)

    def __str__(self):
        return "{}".format(self.office_name)

class CountryRegion(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey('cities_light.Country', null=True)
    region = models.ForeignKey('Region', null=True)

    def __str__(self):
        return "{}, {}".format(self.country, self.region)
