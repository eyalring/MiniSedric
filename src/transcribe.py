""" transcribing audio files using AWS service """
import json
import urllib.request
import datetime
import os
import boto3

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
REGION_NAME = os.environ["REGION_NAME"]

transcribe_client = boto3.client('transcribe', aws_access_key_id=AWS_ACCESS_KEY_ID,
                                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                region_name=REGION_NAME)

def transcribe_audio_file(s3_file_path):
    """Transcribe an audio file from S3 using AWS Transcribe"""
    transcribe_job_name = f'transcribe-job-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'

    transcribe_client.start_transcription_job(
        TranscriptionJobName=transcribe_job_name,
        LanguageCode='en-US',
        MediaFormat='mp3',
        Media={
            'MediaFileUri': s3_file_path 
        }
    )

    while True:
        job = transcribe_client.get_transcription_job(TranscriptionJobName=transcribe_job_name)
        if job['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        
    if(job['TranscriptionJob']['TranscriptionJobStatus'] == 'FAILED'):
        raise Exception('Transcription job failed')
    

    transcription_uri = job['TranscriptionJob']['Transcript']['TranscriptFileUri']
    json_response = urllib.request.urlopen(transcription_uri)
    transcription_as_json = json.load(json_response)
    transcription_text = transcription_as_json['results']['transcripts'][0]['transcript']
    return transcription_text
