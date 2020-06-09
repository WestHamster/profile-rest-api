from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionMixin


class UserProfile(AbstractBaseUser,PermissionMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)   #model is always active
    is_staff = models.BooleanField(default=False)   #Staff user

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'    #by default it takes name but now it will take email
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.name
