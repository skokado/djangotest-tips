from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserManager(BaseUserManager):
    pass


class User(AbstractUser):
    USERNAME_FIELD = 'username'
