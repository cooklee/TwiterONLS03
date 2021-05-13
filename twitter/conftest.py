from django.contrib.auth.models import User
import pytest

from twitter.models import Tweet


@pytest.fixture
def user():
    u = User()
    u.username = 'cooklee'
    u.set_password("vet")
    u.save()
    return u

@pytest.fixture
def two_user():
    users = []
    for x in range(2):
        u = User()
        u.username = f'{x}'
        u.set_password("vet")
        u.save()
        users.append(u)
    return users

@pytest.fixture
def tweets(user):
    ts = []
    for x in range(10):
        t = Tweet()
        t.content = 'jakis content'
        t.creator = user
        t.save()
        ts.append(t)
    return ts


