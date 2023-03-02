from app.views import getMessageV1
import pytest
from django.test import Client
from django.urls import reverse, resolve
from django.contrib.auth.views import LogoutView
from app.views import chat


# create the client function to run the http requests
@pytest.fixture
def client():
    return Client()


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
    # requires follow=True the url for the auth to work.
    response = client.get('/app/chat/', follow=True)
    assert response.status_code == 200


# Test invalid login credentials
@pytest.mark.django_db
def test_login_view_invalid_credentials(client):
    url = reverse('login')
    response = client.post(url, {'username': 'blahblah', 'password': 'wrong_password'})
    assert response.status_code == 200
    assert b'Please enter a correct username and password.' in response.content


# Test the 404 status code
def test_404_handling(client):
    response = client.get('/app/chat/bad_url/')
    assert response.status_code == 404


# test that the chat url returns the correct view
def test_chat_url():
    url = reverse('chat')
    assert resolve(url).func == chat


# Test that the logout url correctly responds with the logout view
def test_logout_url():
    url = reverse('logout')
    assert resolve(url).func.view_class == LogoutView

