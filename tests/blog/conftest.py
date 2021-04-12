import pytest

from tests.account.factories import SuperUserFactory, GeneralUserFactory


@pytest.fixture()
def auto_loggedin_superuser(client):
    user = SuperUserFactory()
    client.login(username='admin-user', password='password')
    yield client, user
    client.logout()


@pytest.fixture()
def auto_loggedin_generaluser(client):
    user = GeneralUserFactory()
    client.login(username='user1', password='password')
    yield client, user
    client.logout()
