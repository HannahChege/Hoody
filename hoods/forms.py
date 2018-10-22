from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import NeighbourHood,Business,Profile


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):

    class Meta:
        model =Profile
        exclude=['user']
class BusinessForm(forms.ModelForm):

    class Meta:
        model =Business
        exclude=['user']    
            
class NewHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ['user']
        widgets = {
            'likes': forms.CheckboxSelectMultiple(),
    }      

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']
        widgets = {
            'likes': forms.CheckboxSelectMultiple(),
    }        