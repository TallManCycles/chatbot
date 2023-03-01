import pytest
from django.contrib.auth import authenticate

from app.views import getMessageV1



# test to check if the bot is responding to the user
def test_bot_response():
    assert getMessageV1('') == 'Hi, how can I help you? type "Book Trip" to begin.'

