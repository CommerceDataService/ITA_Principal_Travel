from django.utils import six
from django.test import TestCase, Client
from .models import *

# Create your tests here.
from registration.models import RegistrationProfile
from registration.users import UserModel


class HeaderResponseTestCase(TestCase):
    def test_content_length(self):
        c = Client()
        response = c.get('/')
        self.assertTrue(int(response['Content-Length']) > 0)
        print(response['Content-Length'])

        response = c.get('/account/login/')
        self.assertTrue(int(response['Content-Length']) > 0)
        print(response['Content-Length'])


# Test Cases for User Registration
class RegistrationModelTests(TestCase):
    user_info = {   'username': 'docemployee',
                    'password': 'letstravel',
                    'email': 'doc@example.com'}
    def test_profile_creation(self):
        # Testing Registration and Profile Creation
        new_user = UserModel().objects.create_user(**self.user_info)
        profile = RegistrationProfile.objects.create_profile(new_user)

        self.assertEqual(RegistrationProfile.objects.count(), 1)
        self.assertEqual(profile.user.id, new_user.id)
        self.assertEqual(six.text_type(profile),
                         "Registration information for docemployee")

    def test_profile_retrieval(self):
        # Testing User Information Retrieval for Login
        new_user = UserModel().objects.create_user(**self.user_info)
        existing_user = UserModel().objects.get(username='docemployee')

        self.failUnless(existing_user.check_password('letstravel'))
        self.assertEqual(existing_user.email, 'doc@example.com')
        self.failUnless(existing_user.is_active)

class ModelStringReprTestCase(TestCase):
    event_info = {
        'host': 'Mary Poppins',
        'name': 'TradeConf 2016',
        'description': 'description',
    }

    principal_info = {
        'first_name': 'Mary',
        'last_name': 'Poppins',
        'title': 'Chief Nanny'
    }

    trip_info = {
        'start_date': '2016-01-01',
        'end_date': '2016-01-05'
    }

    region_info = {
        'name': 'Asia',
    }

    agency_info = {
        'name': 'ITA',
    }

    event_type_info = {
        'name': 'Conference',
    }

    office_info = {
        'short_name': 'NRU',
        'long_name': 'Nannies R Us',
    }

    def test_event_str(self):
        event = Event.objects.create(**self.event_info)
        self.assertEqual('TradeConf 2016', str(event))

    def test_principal_str(self):
        principal = Principal.objects.create(**self.principal_info)
        self.assertEqual('Mary, Poppins, Chief Nanny', str(principal))

    def test_trip_str(self):
        principal = Principal.objects.create(**self.principal_info)
        self.trip_info['principal'] = principal
        trip = Trip.objects.create(**self.trip_info)
        self.assertEqual('2016-01-01 - 2016-01-05', str(trip))

    def test_region_str(self):
        agency = Agency.objects.create(**self.agency_info)
        self.region_info['agency'] = agency
        region = Region.objects.create(**self.region_info)
        self.assertEqual('Asia', str(region))

    def test_event_type_str(self):
        event_type = EventType.objects.create(**self.event_type_info)
        self.assertEqual('Conference', str(event_type))

    def test_agency_str(self):
        agency = Agency.objects.create(**self.agency_info)
        self.assertEqual('ITA', str(agency))

    def test_office(self):
        self.office_info['agency'] = Agency.objects.create(**self.agency_info)
        office = Office.objects.create(**self.office_info)
        self.assertEqual('NRU', str(office))

