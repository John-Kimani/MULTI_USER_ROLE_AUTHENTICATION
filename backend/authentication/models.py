from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    '''
        Class: Overwrites user creation
    '''

    def create_user(self, email, password, **extra_fields):
        '''
            func: Create system users
        '''

        if not email:
            raise ValueError(_("An email should be provided!"))
        
        email = self.normalize_email(email)

        new_user = self.model(email, **extra_fields)

        new_user.set_password()

        new_user.save()

    
