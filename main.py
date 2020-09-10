#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import boto3
import time
import os
import pytest
import json

aws_access_key_id = os.environ["AWS_ACCESS_KEY_ID"] if 'AWS_ACCESS_KEY_ID' in os.environ else 'localstack'
aws_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"] if 'AWS_SECRET_ACCESS_KEY' in os.environ else 'localstack'
endpoint_url = os.environ['ENDPOINT_URL'] if 'ENDPOINT_URL' in os.environ else 'http://localstack:4566'
queue_url = os.environ['SQS_URL'] if 'SQS_URL' in os.environ else 'http://localstack:4566/000000000000/my_queue'

def main():
  
  sqs_client = boto3.client( 'sqs', 
    aws_access_key_id = aws_access_key_id,
    aws_secret_access_key = aws_secret_access_key,
    endpoint_url = endpoint_url
  )

  while True:
    response = sqs_client.receive_message( QueueUrl=queue_url,
      AttributeNames=[
        'SentTimestamp'
      ],
      MaxNumberOfMessages=1,
      MessageAttributeNames=[
        'All'
      ],
      VisibilityTimeout=0,
      WaitTimeSeconds=0
    )
    if 'Messages' in response and len(response['Messages'])==1:
      message = response['Messages'][0]
      file_name = download_file(json.loads(message['Body']))
      if file_name:
        pytest.main(["-x", "content"])
        os.remove(file_name)
      response = sqs_client.delete_message(
        QueueUrl = queue_url,
        ReceiptHandle = message['ReceiptHandle']
      )
    time.sleep(5)

def download_file(message):
  file_name = 'test.py'
  if 's3' in message:
    s3 = boto3.resource('s3', 
      aws_access_key_id = aws_access_key_id,
      aws_secret_access_key = aws_secret_access_key,
      endpoint_url = endpoint_url
    )
    bucket = s3.Bucket(message['s3']['bucket'])
    bucket.download_file(message['s3']['object'], file_name)

    return file_name
  return None
  
if __name__ == "__main__":
  main()
