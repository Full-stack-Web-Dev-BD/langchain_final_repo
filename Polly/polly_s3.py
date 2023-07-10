from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
session = Session(profile_name="adminuser")
polly = session.client("polly")

def generate_speech(bot_response):
    try:
    # Request speech synthesis
        prefix = bot_response
        bad_chars = [';', ':', '!', "*", " ", "'", ",", "."]
        for i in bad_chars:
            prefix = prefix.replace(i, '')
        prefix = prefix[:10]
        response = polly.start_speech_synthesis_task(Engine='neural',
                                                OutputS3KeyPrefix= prefix,
                                                OutputS3BucketName='waterloobucket',
                                                Text= bot_response,
                                                OutputFormat= 'mp3',
                                                VoiceId= 'Amy')
        txt = response['SynthesisTask']['OutputUri']
        fname = txt.split('/')
        pub_url = 'https://waterloobucket.s3.amazonaws.com/' + fname[-1]
        return pub_url    

    except (BotoCoreError, ClientError) as error: 
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)

url = generate_speech("Can you tell us about your relationship with the deceased?")
print(url)