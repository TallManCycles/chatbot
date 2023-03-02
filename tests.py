import pytest
from django.contrib.auth import authenticate

from app.views import getMessageV1
import pytest
from django.test import Client


# test to check if the bot is responding to the user
def test_bot_response():
    assert getMessageV1('') == 'Hi, how can I help you? type "Book Trip" to begin.'


# Test that the django server is running
def test_server_is_running(client):
    response = client.get('/')
    assert response.status_code == 200


# test that the user needs to be logged in to access the chat
@pytest.mark.django_db
def test_permission_required(client):
    # Test that the redirect to home gives a 302 status
    response = client.get('/app/chat/')
    assert response.status_code == 302

    # test that logging in gives a 200 status
    client.login(username='superuser', password='superuser')
    # requires following the url for the auth to work.
    response = client.get('/app/chat/', follow=True)
    assert response.status_code == 200


def test_error_handling(client):
    response = client.get('/app/chat/bad_url/')
    assert response.status_code == 404



