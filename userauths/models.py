from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.CharField(max_length=100,default="No bio provided")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name','username',]  # Corrected field name and using AbstractUser's fields

    def __str__(self):
        return self.email  # Or self.username if you prefer