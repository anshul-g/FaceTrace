from key import access_key, secret_key
from boto3 import s3
import boto3
import os

# accessing S3 storage
client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_key)

# uploading csv files to bucket in S3
for file in os.listdir():
	if '.csv' in file:
		upload_file_bucket = 'dti-project'
		upload_file_key = 'Bennett University/' + str(file)
		client.upload_file(file, upload_file_bucket, upload_file_key)

print("Upload successful")