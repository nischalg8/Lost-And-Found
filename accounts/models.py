from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    roll_no = models.CharField('Campus Roll No',unique=True)
    email = models.EmailField('email address', unique=True)
    phone_number = models.CharField(max_length=25)
 
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.username
    
