from django.db import models
from .User_model import User

class BaseUserProfile(models.Model):
    class Gender(models.TextChoices):
        male   = 'male', 'Male'
        female = 'female', 'Female'
        custom = 'custom', 'custom'


         

    user           = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic    = models.ImageField(upload_to='profile/image/', blank=True, null=True)
    profession     = models.CharField(max_length=250,blank=True,null=True)
    gender         = models.CharField(
        max_length=15,
        choices=Gender.choices,
        blank=True,
        null=True
    )
    location       = models.CharField(blank=True, null=True)
    github_url     = models.URLField(blank=True, null=True)
    linkedin_url   = models.URLField(blank=True, null =True)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

