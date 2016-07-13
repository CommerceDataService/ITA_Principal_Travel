from datetime import datetime
from django.test import TestCase
from cities_light.models import Country
from model_mommy.recipe import seq
from travel.mommy_recipes import region, country, event, trip, COUNTRY_NAMES, REGION_NAMES
from travel.models import Event, Region
from travel.views import _report_queryset_by_attr


class ReportViewTests(TestCase):
    def setUp(self):
        self.maxDiff = None

        region.make(_fill_optional=True, _quantity=4)
        for region_obj in Region.objects.all():
            country.make(_fill_optional=True, agency_region=[region_obj], _quantity=2)

        # no region
        country.make()
        for country_obj in Country.objects.all():
            event.make(cities_light_country=country_obj, _quantity=2)

        for event_obj in Event.objects.all():
            trip.make(events=[event_obj])

    def test_report_queryset_by_attr__countries(self):
        united_states = Country.objects.filter(name='United States')[0]
        thailand = Country.objects.filter(name='Thailand')[0]

        trip1a = trip.make(start_date=datetime(2015, 3, 1), events=[event.make(cities_light_country=united_states)])
        trip1b = trip.make(start_date=datetime(2015, 4, 1), events=[event.make(cities_light_country=united_states)])
        trip1c = trip.make(start_date=datetime(2015, 4, 1), events=[event.make(cities_light_country=united_states)])
        trip2a = trip.make(start_date=datetime(2015, 1, 1), events=[event.make(cities_light_country=thailand)])
        trip2b = trip.make(start_date=datetime(2015, 1, 1), events=[event.make(cities_light_country=thailand)])

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
        self.assertEqual(Country.objects.count(), 9)
        result = [
            {'count': 1, 'country_id': 1, 'country_name': 'India', 'month': 9},
            {'count': 1, 'country_id': 1, 'country_name': 'India', 'month': 10},
            {'count': 3, 'country_id': 2, 'country_name': 'Thailand', 'month': 1},
            {'count': 1, 'country_id': 2, 'country_name': 'Thailand', 'month': 2},
            {'count': 2, 'country_id': 3, 'country_name': 'United States', 'month': 3},
            {'count': 3, 'country_id': 3, 'country_name': 'United States', 'month': 4},
            {'count': 1, 'country_id': 4, 'country_name': 'Canada', 'month': 5},
            {'count': 1, 'country_id': 4, 'country_name': 'Canada', 'month': 6},
            {'count': 1, 'country_id': 5, 'country_name': 'Belgium', 'month': 3},
            {'count': 1, 'country_id': 5, 'country_name': 'Belgium', 'month': 4},
            {'count': 1, 'country_id': 6, 'country_name': 'Germany', 'month': 7},
            {'count': 1, 'country_id': 6, 'country_name': 'Germany', 'month': 8},
            {'count': 1, 'country_id': 7, 'country_name': 'Madagascar', 'month': 11},
            {'count': 1, 'country_id': 7, 'country_name': 'Madagascar', 'month': 12},
            {'count': 1, 'country_id': 8, 'country_name': 'Zambia', 'month': 5},
            {'count': 1, 'country_id': 8, 'country_name': 'Zambia', 'month': 6},
            {'count': 1, 'country_id': 9, 'country_name': 'Australia', 'month': 1},
            {'count': 1, 'country_id': 9, 'country_name': 'Australia', 'month': 2},
        ]
        self.assertEqual(list(queryset), result)

    def test_report_queryset_by_attr__regions(self):
        # create countries
        bangladesh = country.make(name='Bangladesh')
        china_country = country.make(name='China')

        # pull already-created countries
        united_states = Country.objects.filter(name='United States')[0]

        # pull already-created regions
        americas = Region.objects.filter(name='Americas').all()[0]
        #china_region = Region.objects.filter(name='China').all()[0]
        #china.agency_region_set.add(china_region)

        # now bangladesh and china should be the region-less countries

        trip1a = trip.make(start_date=datetime(2015, 1, 1), events=[event.make(cities_light_country=united_states)])
        trip1b = trip.make(start_date=datetime(2015, 8, 1), events=[event.make(cities_light_country=united_states)])
        trip1c = trip.make(start_date=datetime(2015, 8, 1), events=[event.make(cities_light_country=united_states)])
        trip2a = trip.make(start_date=datetime(2015, 7, 1), events=[event.make(cities_light_country=china_country)])
        trip2b = trip.make(start_date=datetime(2015, 2, 1), events=[event.make(cities_light_country=china_country)])
        trip3a = trip.make(start_date=datetime(2015, 7, 1), events=[event.make(cities_light_country=bangladesh)])
        trip3b = trip.make(start_date=datetime(2015, 12, 1), events=[event.make(cities_light_country=bangladesh)])

        queryset = _report_queryset_by_attr(
            current_year=2015,
            attr_set=REGION_NAMES,
            orig_name='events__cities_light_country__agency_region__name',
            orig_id='events__cities_light_country__agency_region__id',
            new_name='region_name',
            new_id='region_id'
        )
        print(queryset.query)
        self.assertEqual(Region.objects.count(), 4)
        result = [
            {'count': 1, 'region_id': 6, 'region_name': 'Asia', 'month': 1},
            {'count': 1, 'region_id': 6, 'region_name': 'Asia', 'month': 2},
            {'count': 1, 'region_id': 6, 'region_name': 'Asia', 'month': 9},
            {'count': 1, 'region_id': 6, 'region_name': 'Asia', 'month': 10},
            {'count': 1, 'region_id': 7, 'region_name': 'Americas', 'month': 1},
            {'count': 1, 'region_id': 7, 'region_name': 'Americas', 'month': 3},
            {'count': 1, 'region_id': 7, 'region_name': 'Americas', 'month': 4},
            {'count': 1, 'region_id': 7, 'region_name': 'Americas', 'month': 5},
            {'count': 1, 'region_id': 7, 'region_name': 'Americas', 'month': 6},
            {'count': 2, 'region_id': 7, 'region_name': 'Americas', 'month': 8},
	    {'count': 1, 'region_id': 8, 'region_name': 'Europe', 'month': 3, },
	    {'count': 1, 'region_id': 8, 'region_name': 'Europe', 'month': 4, },
	    {'count': 1, 'region_id': 8, 'region_name': 'Europe', 'month': 7, },
	    {'count': 1, 'region_id': 8, 'region_name': 'Europe', 'month': 8, },
	    {'count': 1, 'region_id': 9, 'region_name': 'Africa', 'month': 5, },
	    {'count': 1, 'region_id': 9, 'region_name': 'Africa', 'month': 6, },
	    {'count': 1, 'region_id': 9, 'region_name': 'Africa', 'month': 11},
	    {'count': 1, 'region_id': 9, 'region_name': 'Africa', 'month': 12}
        ]
        self.assertEqual(list(queryset), result)
