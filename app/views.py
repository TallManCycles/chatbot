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

    os.environ['AWS_ACCESS_KEY_ID'] = config['default']['aws_access_key_id']
    os.environ['AWS_SECRET_ACCESS_KEY'] = config['default']['aws_secret_access_key']

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

# Why am I getting: An error occurred (InvalidSignatureException) when calling the RecognizeText operation: The request signature we calculated does not match the signature you provided. Check your AWS Secret Access Key and signing method. Consult the service documentation for details.
# a: