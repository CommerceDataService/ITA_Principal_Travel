# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Event(models.Model):
    eventid = models.AutoField(primary_key=True)
    host = models.CharField(max_length=-1, blank=True, null=True)
    event_description = models.CharField(max_length=-1, blank=True, null=True)
    iga_leg = models.CharField(max_length=-1, blank=True, null=True)
    press = models.NullBooleanField()
    press_note = models.CharField(max_length=-1, blank=True, null=True)
    no_of_travelers = models.IntegerField(blank=True, null=True)
    no_of_travelers_note = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class EventLocPrincipalTravel(models.Model):
    eventid = models.IntegerField(blank=True, null=True)
    locationid = models.IntegerField(blank=True, null=True)
    travelid = models.IntegerField(blank=True, null=True)
    principalid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_loc_principal_travel'


class EventLocation(models.Model):
    eventid = models.IntegerField(blank=True, null=True)
    locationid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_location'


class Location(models.Model):
    locationid = models.AutoField(primary_key=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    country = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class Principal(models.Model):
    principalid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    title = models.CharField(max_length=-1, blank=True, null=True)
    agency = models.CharField(max_length=-1, blank=True, null=True)
    principal_poc = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'principal'


class PrincipalTravel(models.Model):
    travelid = models.IntegerField(blank=True, null=True)
    principalid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'principal_travel'


class Travel(models.Model):
    travelid = models.AutoField(primary_key=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=-1, blank=True, null=True)
    format = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel'
