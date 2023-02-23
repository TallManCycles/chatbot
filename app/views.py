import email.message

from django.shortcuts import render
import boto3

# create a list of bot responses to the user
responses = []


def chat(request):
    # for each request, get the message from the user and add it to the response array
    if request.method == 'POST':
        text = request.POST.get('message', '')
        responses.append(text)
    else:
        text = ''
        responses.clear()

    # get the bot's response to the user's message
    message = getMessage(text)

    # add the bot's response to the response array
    responses.append(message)

    # create a dictionary of the response array
    conversations = {'conversations': responses}

    context = conversations

    return render(request, 'chat.html', context)


def getMessage(input):
    if input == '':
        return 'Hi, how can I help you?'

    client = boto3.client('lexv2-runtime', region_name='ap-southeast-2')

    response = client.recognize_text(
        botId='QSTRXSV9V7',
        botAliasId='TSTALIASID',
        localeId='en_US',
        sessionId="test_session",
        text=input)

    print(response)

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        if 'messages' in response and response['messages']:
            # return the first message
            return response['messages'][0]['content']
        else:
            return 'Thanks! Have a great day!'
    else:
        return 'Sorry, there seems to be a connection issue. Please try again later.'
