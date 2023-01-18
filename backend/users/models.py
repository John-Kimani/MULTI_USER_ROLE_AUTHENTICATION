from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

class CustomUserManager(BaseUserManager):
    '''
        Class that overwrites user creation method
    '''

    def create_user(self, email, password, **extra_fields):
        '''
            Func: Creates system users
        '''
        if not email:
            raise ValueError(_("Email should be provided."))
        email = self.normalize_email(email)

        new_user = self.model(email, **extra_fields)

        new_user.set_password(password)

        new_user.save()

        return new_user
    
    def create_superuser(self, email, password, **extra_fields):
        '''
            Func: Create system admin
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        ## Validate super user instance
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("The superuser account should have is_staff as True."))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("The superuser account should have is_superuser as True."))
        
        if extra_fields.get('is_active') is not True:
            raise ValueError(_("The superuser account should have is_active as True."))
        
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractUser):
    '''
    Class that redefines user instance for the entire application
    '''
    username=models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=65, unique=True)

    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['username']

    objects=CustomUserManager()

    def __str__(self):
        return f'User: {self.username}'

class Role(models.Model):
    '''
    Class to define employee roles
    '''
    pass