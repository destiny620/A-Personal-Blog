from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'image', 'bio', 'phone_no', 'email', 'facebook', 'twitter', 'instagram', 'linkedin']
       

class BlogpostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'slug', 'content', 'image', 'created_at']

class Editprofileform(forms.ModelForm):
    class Meta:
        model=Profile
        fields= fields = ['user', 'image', 'bio', 'phone_no', 'email', 'facebook', 'twitter', 'instagram', 'linkedin']

class EditBlogPostform(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields= fields = ['title', 'author', 'slug', 'content', 'image', 'created_at']
       
       
