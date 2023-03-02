from django.shortcuts import render
import boto3
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def handler404(request, exception):
    return render(request, '404.html', status=404)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat/')
        else:
            error = 'Invalid login credentials'
    else:
        error = ''
    return render(request, 'login.html', {'error': error})


# create a list of bot responses to the user
responses = []


@login_required
def chat(request):
    # for each request, get the message from the user and add it to the response array
    if request.method == 'POST':
        text = request.POST.get('message', '')
        responses.append(text)
    else:
        text = ''
        responses.clear()

    # get the bot's response to the user's message
    message = getMessageV1(text)

    # add the bot's response to the response array
    responses.append(message)

    # create a dictionary of the response array
    conversations = {'conversations': responses}

    context = conversations

    print(context)

    return render(request, 'chat.html', context)


def getMessageV1(input):

    if input == '':
        return 'Hi, how can I help you? type "Book Trip" to begin.'

    client = boto3.client('lex-runtime', region_name='ap-southeast-2')

    response = client.post_text(
        botName='AlexVONE',
        botAlias='VersionOne',
        userId='663080568213',
        inputText=input
    )

    return response['message']

