from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from  .models import Profile



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

