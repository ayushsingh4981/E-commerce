from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Corrected field name and using AbstractUser's fields

    def __str__(self):
        return self.email  # Or self.username if you prefer