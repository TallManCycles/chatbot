import boto3

import os
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZUYVOQWKVECYWX6H'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'

client = boto3.client('lexv2-runtime', region_name='ap-southeast-2')

response = client.recognize_text(
    botId='WHJUECIRUH',
    botAliasId='TSTALIASID',
    localeId='en_US',
    sessionId="test_session",
    text='Book a trip')

print(response['messages'][0]['content'])




