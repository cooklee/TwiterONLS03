from django.contrib.auth.models import User
from django.test import Client
import pytest
from django.urls import reverse

from twitter.models import Tweet, Message


@pytest.mark.django_db
def test_client():
    Client()


@pytest.mark.django_db
def test_index_view_get(tweets):
    c = Client()
    url = reverse('index')
    response = c.get(url)
    tweets = response.context['tweets']
    assert response.status_code == 200
    assert tweets.count() == len(tweets)


@pytest.mark.django_db
def test_add_tweet_get_not_logged_in(user):
    c = Client()
    url = reverse('add_tweet')
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_add_tweet_get_logged_in(user):
    c = Client()
    c.force_login(user)
    url = reverse('add_tweet')
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_tweet_post(user):
    c = Client()
    c.force_login(user)
    url = reverse('add_tweet')
    response = c.post(url, {'content': 'alamakota'})
    assert response.status_code == 302
    assert Tweet.objects.count() == 1


@pytest.mark.django_db
def test_add_message_get_not_logged_in():
    c = Client()
    url = reverse('add_message')
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_add_message_get_logged_in(user):
    c = Client()
    c.force_login(user)
    url = reverse('add_message')
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_tweet_message(two_user):
    c = Client()
    c.force_login(two_user[0])
    url = reverse('add_message')
    response = c.post(url, {'text': 'alamakota', 'to_user': two_user[1].pk})
    assert response.status_code == 302
    assert Message.objects.count() == 1
