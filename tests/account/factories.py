from factory.django import DjangoModelFactory
from django.contrib.auth.hashers import make_password

from account.models import User


class SuperUserFactory(DjangoModelFactory):
    username = 'admin-user'
    password = make_password('password')
    is_staff = True
    is_superuser = True

    class Meta:
        model = User


class GeneralUserFactory(DjangoModelFactory):
    username = 'user1'
    password = make_password('password')
    is_staff = True
    is_superuser = False

    class Meta:
        model = User
