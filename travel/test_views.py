import pytest
import datetime
from cities_light.models import Country
from django.test import TestCase
from travel.models import Event, Region
from travel.views import _report_queryset_by_attr
from model_mommy import mommy
from travel.mommy_recipes import *


class ReportViewTests(TestCase):
    def setUp(self):
        self.maxDiff = None

        # region.make(_quantity=5)
        # for region_obj in Region.objects.all():
        #     country.make(_fill_optional=True, agency_region=region_obj)

        country.make(_quantity=6)
        for country_obj in Country.objects.all():
            event.make(cities_light_country=country_obj, _quantity=2)

        for event_obj in Event.objects.all():
            trip.make(events=[event_obj])

    def test_report_queryset_by_attr__countries(self):
        queryset = _report_queryset_by_attr(
            current_year=2015,
            attr_set=COUNTRY_NAMES,
            orig_name='events__cities_light_country__name',
            orig_id='events__cities_light_country__id',
            new_name='country_name',
            new_id='country_id'
        )
        # Leaving for debugging
        # print(queryset.query)
        self.assertEqual(Country.objects.count(), 6)
        result = [
            {'count': 1, 'country_id': 1, 'country_name': 'India', 'month': 5},
            {'count': 1, 'country_id': 1, 'country_name': 'India', 'month': 6},
            {'count': 1, 'country_id': 2, 'country_name': 'United States', 'month': 9},
            {'count': 1, 'country_id': 2, 'country_name': 'United States', 'month': 10},
            {'count': 1, 'country_id': 3, 'country_name': 'Belgium', 'month': 1},
            {'count': 1, 'country_id': 3, 'country_name': 'Belgium', 'month': 2},
            {'count': 1, 'country_id': 4, 'country_name': 'Madagascar', 'month': 7},
            {'count': 1, 'country_id': 4, 'country_name': 'Madagascar', 'month': 8},
            {'count': 1, 'country_id': 5, 'country_name': 'Canada', 'month': 3},
            {'count': 1, 'country_id': 5, 'country_name': 'Canada', 'month': 4},
            {'count': 1, 'country_id': 6, 'country_name': 'Zambia', 'month': 11},
            {'count': 1, 'country_id': 6, 'country_name': 'Zambia', 'month': 12}
        ]
        self.assertEqual(list(queryset), result)

    @pytest.mark.skip('Need to figure out the right way to set up the test data')
    def test_report_queryset_by_attr__regions(self):
        queryset = _report_queryset_by_attr(
            current_year=2015,
            attr_set=REGION_NAMES,
            orig_name='events__cities_light_country__agency_region__name',
            orig_id='events__cities_light_country__agency_region__id',
            new_name='region_name',
            new_id='region_id'
        )
        self.assertEqual(Region.objects.count(), 5)
        result = [
            {'count': 1, 'region_id': 1, 'region_name': 'India', 'month': 5},
            {'count': 1, 'region_id': 2, 'region_name': 'United States', 'month': 9},
            {'count': 1, 'region_id': 3, 'region_name': 'Belgium', 'month': 1},
            {'count': 1, 'region_id': 4, 'region_name': 'Madagascar', 'month': 7},
            {'count': 1, 'region_id': 5, 'region_name': 'Canada', 'month': 3},
            {'count': 1, 'region_id': 6, 'region_name': 'Zambia', 'month': 11},
        ]
        self.assertEqual(list(queryset), result)
