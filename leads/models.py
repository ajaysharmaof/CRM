from django.db import models
"""
An abstract base class implementing a fully featured User model with
admin-compliant permissions.

Username and password are required. Other fields are optional.
"""
from django.contrib.auth.models import AbstractUser

#from django.contrib.auth import get_user_model      #default built in user model by django
#User = get_user_model()

class User(AbstractUser):
    pass

class Lead(models.Model):

    #SOURCE_CHOICES = (
    #    ('YouTube', 'YouTube'),
    #    ('Google', 'Google'),
    #   ('Newsletter', 'Newsletter'),
    #)
    #phoned     = models.BooleanField(default=False)
    #source     = models.CharField(choices=SOURCE_ CHOICES, max_length=100)
    
    #profile_pic = models.ImageField(blank=True, null=True)

    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    age        = models.IntegerField(default=0)
    agent      = models.ForeignKey("Agent",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
     

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #one user associate with one agent

    def __str__(self):
        return self.user.email



 
