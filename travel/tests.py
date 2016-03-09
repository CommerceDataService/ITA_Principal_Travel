from django.utils import six
from django.test import TestCase

# Create your tests here.
from registration.models import RegistrationProfile
from registration.users import UserModel

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

class TestTestCase(TestCase):
    def test_test(self):
        assert 1
