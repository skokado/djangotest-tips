from django.test import Client
import pytest

from account.models import User
from tests.account.factories import SuperUserFactory


@pytest.mark.django_db
def test_login_adminsite(client):
    user = SuperUserFactory()
    logged_in = client.login(username='admin-user', password='password')
    assert logged_in is True

    response = client.get('/admin/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_fail(client):
    user = SuperUserFactory()
    logged_in = client.login(username='admin-user', password='incorrect')
    assert logged_in is False
