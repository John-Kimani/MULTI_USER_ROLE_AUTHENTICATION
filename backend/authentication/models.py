from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        '''
            Func: Overwrite user creation
        '''
        if not email:
            raise ValueError(_("Email should be provided!"))
        
        email = self.normalize_email(email)

        new_user = self.model(email, **extra_fields)

        new_user.set_password(password)

        new_user.save()

        return new_user

    def create_superuser(self, email, password, **extra_fields):
        '''
            Func: Overwrite create superuser
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser account should have is_staff is True.'))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser account should have is_superuser is True.'))
        
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser account should have is_active is True.'))
        
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractUser):
    '''
        Class to create user instances
    '''
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    phone_number = PhoneNumberField(null=False, unique=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS=['username','phone_number']

    def __str__(self):
        return f"<user {self.username}"