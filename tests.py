import pytest
from app.views import getMessageV2


# write a test to check if the bot is responding to the user
def test_bot_response():
    assert getMessageV2('') == 'Hi, how can I help you? type "Book Trip" to begin.'