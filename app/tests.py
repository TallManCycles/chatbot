import configparser

from django.test import TestCase

config = configparser.ConfigParser()
config.read('aws_credentials.txt')

print(config['default']['aws_access_key_id'])
print(config['default']['aws_secret_access_key'])
