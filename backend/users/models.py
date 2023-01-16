from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    '''
    Class that redefines user instance for the entire application
    '''
    email = models.EmailField(unique=True)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)

class Role(models.Model):
    '''
    Class to define employee roles
    '''
    pass