from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length =30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()


    @receiver(post_save,sender=User)
    def create_profile(sender, instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_profile(sender, instance,**kwargs):
        instance.profile.save()
    def __str__(self):
        return self.user.username
    def save_profile(self):
        self.save()  

    def delete_profile(self):
        self.delete()  

    @classmethod
    def update_profile(cls,update):
        pass
     
    @classmethod
    def search_by_profile(cls,name):
        profile = Profile.objects.filter(user__username__icontains=name)
        return profile 
    @classmethod 
    def get_by_id(cls,id):
        profile = Profile.objects.get(user = id)
        return profile


class NeighbourHood(models.Model):
    name = models.CharField(max_length =30)
    location= models.CharField(max_length =30)
    Occupants_Count= models.CharField(max_length = 30, blank=True)
    user = models.ForeignKey(User)
   
    def __str__(self):
        return self.user.username

    def save_neigborhood(self):
        self.save()  

    def delete_neigborhood(self):
        self.delete()  

    @classmethod
    def update_neigborhood(cls,update):
        pass
     
    @classmethod
    def search_by_neigborhood(cls,name):
        neigborhood = Neigborhood.objects.filter(user__username__icontains=name)
        return neigborhood
    @classmethod 
    def get_by_id(cls,id):
        neigborhood = Neigborhood.objects.get(user = id)
        return neigborhood       


class Business(models.Model):
    business_name = models.CharField(max_length =30)
    business_email = models.EmailField()
    user = models.ForeignKey(User)
   
    def __str__(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        return self.user.username

    def save_business(self):
        self.save()  

    def delete_business(self):
        self.delete()  

    @classmethod
    def update_business(cls,update):
        pass
     
    @classmethod
    def search_by_business(cls,name):
        business= Business.objects.filter(user__username__icontains=name)
        return business
    @classmethod 
    def get_by_id(cls,id):
        business = Business.objects.get(user = id)
        return business