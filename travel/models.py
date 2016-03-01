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

    def __str__(self):
        return "{}".format(self.event_description)

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{}, {}, {}".format(self.city, self.state, self.country)

class Principal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    agency = models.CharField(max_length=255, blank=True, null=True)
    principal_poc = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.title, self.agency)

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

