from users.models import Profile
from django.db import models
import uuid

class Project(models.Model):
      owner = models.ForeignKey(Profile,null=True,blank=True, on_delete=models.SET_NULL)
      title= models.CharField(max_length=200)
      discription= models.TextField(null=True,blank=True)
      featured_images= models.ImageField(null=True,blank=True,default="default.jpg")
      demo_link=models.CharField(max_length=2000,null=True,blank=True)
      source_link=models.CharField(max_length=2000,null=True,blank=True)
      tag=models.ManyToManyField('Tag',blank=True)#if the tag class is above the project class you don't have to quote them.  
      vote_total=models.IntegerField(default=0,null=True,blank=True)
      vote_ratio=models.IntegerField(default=0,null=True,blank=True)
      created=models.DateTimeField(auto_now_add=True)
      id=models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)
      def __str__(self):#..this is used to change the project title  into string form
         return self.title
      
      class Meta:
          ordering = ['created'] #used for ascending the Project based on the time it is posted


class Review(models.Model):
     VOTE_TYPE=(
     ('up','up vote'), #this means (actual value, human readable value)
     ('down','Down vote'),
     )
     Project= models.ForeignKey(Project, on_delete=models.CASCADE)
     body = models.TextField(null=True, blank=True)
     value= models.CharField(max_length=200,choices=VOTE_TYPE)
     created=models.DateTimeField(auto_now_add=True)
     id=models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)
     def __str__(self) -> str:
          return self.value
class Tag(models.Model):
     name=models.CharField(max_length=200)
     created=models.DateTimeField(auto_now_add=True)
     id=models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=True)
     def __str__(self) -> str:
          return self.name
     
