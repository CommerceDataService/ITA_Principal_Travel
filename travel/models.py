# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    event_description = models.TextField(blank=True, null=True)
    iga_leg = models.CharField(max_length=10, blank=True, null=True)
    press = models.NullBooleanField()
    press_note = models.CharField(max_length=255, blank=True, null=True)
    no_of_travelers = models.IntegerField(blank=True, null=True)
    no_of_travelers_note = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class EventLocPrincipalTravel(models.Model):
    event_id = models.ForeignKey('Event')
    location_id = models.ForeignKey('Location')
    travel_id = models.ForeignKey('Travel')
    principal_id = models.ForeignKey('Principal')

    class Meta:
        managed = False
        db_table = 'event_loc_principal_travel'


class EventLocation(models.Model):
    event_id = models.ForeignKey('Event')
    location_id = models.ForeignKey('Location')

    class Meta:
        managed = False
        db_table = 'event_location'


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class Principal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    agency = models.CharField(max_length=255, blank=True, null=True)
    principal_poc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'principal'


class PrincipalTravel(models.Model):
    travel_id = models.ForeignKey('Travel')
    principal_id = models.ForeignKey('Principal')

    class Meta:
        managed = False
        db_table = 'principal_travel'


class Travel(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=32, blank=True, null=True)
    format = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel'
