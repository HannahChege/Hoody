from django.test import TestCase
from .models import Profile,NeighbourHood,Business,Post
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
        new_profile = Profile.objects.filter(email='chegehannah45@gmail.com').update(email='njerichege@gmail.com')

    
    def test_get_profile_by_id(self):
        """
        Function to test if you can get a profile by its id
        """
        self.profile.save_profile()
        this_pro= self.profile.get_by_id(self.profile.user_id)
        profile = Profile.objects.get(user_id=self.profile.user_id)
        self.assertTrue(this_pro, profile)

class NeighbourHoodTestClass(TestCase):
    """
    Test NeighbourHoodclass and its functions
    """
    def setUp(self):
        self.hood = NeighbourHood(name='hannah', location='kilimani', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.hood, NeighbourHood)

    

    def test_delete_method(self):
        """
        Function to test that a neighbourhood can be deleted
        """
        self.hood.save_hood()
        self.hood.delete_hood

    def test_update_method(self):
        """
        Function to test that a neighbourhood's details can be updated
        """
        self.hood.save_hood()
        new_hood = NeighbourHood.objects.filter(name='mtaani').update(name='Bias')
        hoods = NeighbourHood.objects.get(name='cookie')
        self.assertTrue(hoods.name, 'cookie')

    
    def test_get_by_id(self):
        """
        Function to test if you can get a hood by its id
        """
        self.hood.save_hood()
        this_hood= self.hood.get_by_id(self.hood.id)
        hood = NeighbourHood.objects.get(id=self.hood.id)
        self.assertTrue(this_hood, hood)


class BusinessTestClass(TestCase):
    """
    Test business class and its functions
    """
    def setUp(self):
        self.user = User.objects.create(id =1, username='a')
        self.hood = Neighbour(name='hannah', location='kilamani', user=self.user)
        self.hood.save_hood()
        self.business = Business(name="cookie", email="cookie@gmail.com", user=self.user, hood=self.hood)

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    
    def test_save_method(self):
        """
        Function to test that neighbourhood is being saved
        """
        self.business.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_method(self):
        """
        Function to test that a neighbourhood can be deleted
        """
        self.business.save_business()
        self.business.delete_business()

    def test_update_method(self):
        """
        Function to test that a neighbourhood's details can be updated
        """
        self.business.save_business()
        new_business = Business.objects.filter(name='cookie').update(name='business')
        business = Business.objects.get(name='cookie')
        self.assertTrue(business.name, 'cookie')


    def test_get_by_id(self):
        """
        Function to test if you can get a hood by its id
        """
        self.business.save_business()
        this_business= self.business.get_by_businessid(self.business.id)
        business = Business.objects.get(id=self.business.id)
        self.assertTrue(this_business, business)



class PostsTestClass(TestCase):
    """
    Test posts class and its functions
    """
    def setUp(self):
        self.user = User.objects.create(id =1, username='a')
        self.hood = Neighbour(location='kiliani', Description='Peace full hood', user=self.user)
        self.hood.save_hood()
        self.post = Posts(location="business", user=self.user, hood=self.hood)

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Posts))

    
    def test_save_method(self):
        """
        Function to test that a post is being saved
        """
        self.post.save_posts()
        posts = Posts.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        """
        Function to test that a neighbourhood can be deleted
        """
        self.post.save_posts()
        self.post.del_posts()

    def test_update_method(self):
        """
        Function to test that a post's details can be updated
        """
        self.post.save_posts()
        new_posts = Posts.objects.filter(location='kilimani').update(location='adams')
        business = Posts.objects.get(location='kilimani')
        self.assertTrue(business.location, 'kilimani')

        
 
