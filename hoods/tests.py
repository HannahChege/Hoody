from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
# Create your tests here.

class ProfileTestClass(TestCase):
    """
    Test profile class and its functions
    """
    def setUp(self):

        self.user = User.objects.create(id =1,username='hannah')
        self.profile = Profile(email='chegehannah45@gmail.com', name='hannah',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        """
        Function to test that profile is being saved
        """
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        """
        Function to test that a profile can be deleted
        """
        self.profile.save_profile()
        

    def test_update_method(self):
        """
        Function to test that a profile's details can be updated
        """
        self.profile.save_profile()
        new_profile = Profile.objects.filter(bio='chegehannah45@gmail.com').update(email='njerichege@gmail.com')

    
    def test_get_profile_by_id(self):
        """
        Function to test if you can get a profile by its id
        """
        self.profile.save_profile()
        this_pro= self.profile.get_by_id(self.profile.user_id)
        profile = Profile.objects.get(user_id=self.profile.user_id)
        self.assertTrue(this_pro, profile)
