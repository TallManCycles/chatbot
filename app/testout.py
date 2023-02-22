import boto3
import os
import configparser

config = configparser.ConfigParser()
config.read('aws_credentials.txt')

print(config['default']['aws_access_key_id'])

# os.environ['AWS_ACCESS_KEY_ID'] = config['default']['aws_access_key_id']
# os.environ['AWS_SECRET_ACCESS_KEY'] = config['default']['aws_secret_access_key']