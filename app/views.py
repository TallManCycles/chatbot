from django.shortcuts import render
import boto3
import os
import configparser


# Create your views here.
def index(request):
    return render(request, 'index.html')


def records(request):
    return render(request, 'records.html')


def chat(request):

    config = configparser.ConfigParser()
    config.read('aws_credentials.txt')

    aws_access_key_id = os.environ.get('access_key_id')
    aws_secret_access_key = os.environ.get('secret_access_key')

    # aws_access_key_id = config['default']['aws_access_key_id']
    # aws_secret_access_key = config['default']['aws_secret_access_key']

    os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
    os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key

    client = boto3.client('lexv2-runtime', region_name='ap-southeast-2')

    response = client.recognize_text(
        botId='WHJUECIRUH',
        botAliasId='TSTALIASID',
        localeId='en_US',
        sessionId="test_session",
        text='Book a trip')

    message = response['messages'][0]['content']

    context = {'message': message}

    return render(request, 'chat.html', context)