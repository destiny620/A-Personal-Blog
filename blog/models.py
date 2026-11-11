from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    twitter = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)
    
    # def get_absolute_url(self):
    #     return reverse('home')

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.CharField(max_length=130)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
   
    

    def __str__(self):
        return(self.title)
    
    def get_absolute_url(self):
        return reverse('home')
    
    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)
            unique_slug = self.slug
            counter = 1
            if BlogPost.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{counter}'
                counter += 1
            self.slug = unique_slug
        
        super().save(*args, **kwargs)