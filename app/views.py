from django.shortcuts import render
import boto3

# os.environ['AWS_ACCESS_KEY_ID'] = os.environ.get('AWS_ACCESS_KEY_ID')
# os.environ['AWS_SECRET_ACCESS_KEY'] = os.environ.get('AWS_SECRET_ACCESS_KEY')


def chat(request):
    text = ''

    if request.method == 'POST':
        text = request.POST.get('message', '')

    message = getMessage(text)
    context = {'message': message}

    return render(request, 'chat.html', context)





def getMessage(input):

    if input == '':
        return 'Hi, how can I help you?'

    client = boto3.client('lexv2-runtime', region_name='ap-southeast-2')

    response = client.recognize_text(
        botId='WHJUECIRUH',
        botAliasId='TSTALIASID',
        localeId='en_US',
        sessionId="test_session",
        text=input)

    try:
        # check if response messages is not empty
        if response['messages']:
            # return the first message
            return response['messages'][0]['content']
        else:
            return 'complete'
    except:
        return 'Thank you! Have a nice day!'

