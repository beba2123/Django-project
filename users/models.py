import uuid
from django.db import models
from django.contrib.auth.models import User
from  django.db.models.signals import post_save, post_delete
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    Location = models.CharField(max_length=200, blank=True, null=True) 
    bio = models.TextField(blank=True,null=True)
    Profile_images = models.ImageField(null=True,blank=False,upload_to='profiles/', default='profiles/user-default.png')
    social_github = models.CharField(max_length=200,blank=True, null=True)
    social_linkedin =  models.CharField(max_length=200,blank=True, null=True)
    social_Youtube =  models.CharField(max_length=200,blank=True, null=True)
    social_website = models.CharField(max_length=200,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)
    def __str__(self):#..this is used to change the user title  into string form
         return str(self.username)

class Skill(models.Model):
     owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
     name = models.CharField(max_length=200, blank=True, null=True)
     discription = models.TextField(blank=True, null=True)
     created=models.DateTimeField(auto_now_add=True)
     id=models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)
     def __str__(self):#..this is used to change the user title  into string form
         return str(self.name)


def createProfile(sender, instance, created, **kwargs): 
     if created:
          user = instance
          profile = Profile.objects.create(
               user = user,
               username = user.username,
               email = user.email
          )
def userDelete(sender, instance, **kwargs):
     user = instance.user
     user.delete()
     print('profile and user deleted..!!')

post_save.connect(createProfile, sender=User)
post_delete.connect(userDelete, sender=Profile)

