#This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models
from cities_light.models import Country
from django.contrib.auth.models import User
from author.decorators import with_author

class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add = True, null=True)
    edited_on = models.DateTimeField(auto_now = True, null=True)
    class Meta:
        abstract = True

@with_author #adds and maintains 'author' and 'updated_by' fields
class Event(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    event_type = models.ForeignKey('EventType',null=True)
    press = models.NullBooleanField()
    press_note = models.CharField(max_length=255, blank=True, null=True)
    cities_light_city = models.ForeignKey('cities_light.City',null=True)
    cities_light_country = models.ForeignKey('cities_light.Country',null=True)

    def __str__(self):
        return "{}".format(self.name)

@with_author
class Principal(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    office = models.ForeignKey('Office', null=True)
    career = models.BooleanField(default=False)
    region = models.ForeignKey('Region', null=True)

    def __str__(self):
        return "{}, {}, {}".format(self.first_name, self.last_name, self.title)

@with_author
class Trip(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    no_of_travelers = models.IntegerField(blank=True, null=True)
    no_of_travelers_note = models.CharField(max_length=32, blank=True, null=True)
    principal = models.ForeignKey('Principal', null=False)
    events = models.ManyToManyField('Event')

    @property
    def country(self):
        city_List = [x.cities_light_country for x in self.events.all()]
        update_city_List = [str(name) for name in city_List]
        return ', '.join(update_city_List)

    @property
    def event_name(self):
        event_List = [x.name for x in self.events.all()]
        update_event_List = [str(name) for name in event_List]
        return ', '.join(update_event_List)


    def __str__(self):
        return "{} - {}".format(self.start_date, self.end_date)


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    agency = models.ForeignKey('Agency', null=True)
    countries = models.ManyToManyField(Country, related_name="custom_region")

    def __str__(self):
        return "{}".format(self.name)


class EventType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return "{}".format(self.name)


class Agency(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{}".format(self.name)


class Office(models.Model):
    id = models.AutoField(primary_key=True)
    short_name = models.CharField(max_length=50, null=True)
    long_name = models.CharField(max_length=255, null=True)
    agency = models.ForeignKey('Agency', null=True)

    def __str__(self):
        return "{}".format(self.short_name)
