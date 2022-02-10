from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# Custom User model inherits from parent class, AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    avatar = models.CharField(max_length=500)
    # Require email field for authentication
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    # Override get_username method by returning email
    def get_username(self):
        return self.email
