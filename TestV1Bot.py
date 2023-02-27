import boto3
from dotenv import load_dotenv
load_dotenv()

client = boto3.client('lex-runtime', region_name='ap-southeast-2')

response = client.post_text(
    botName='AlexVONE',
    botAlias='VersionOne',
    userId='AKIAZUYVOQWKVECYWX6H',
    inputText="Book trip"
)

print(response['message'])