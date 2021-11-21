from django.shortcuts import render
from botocore.client import Config
from django.contrib.auth.decorators import login_required
import boto3


# Create your views here.
@login_required(login_url='/')
def dashboard(request): 
    s3 = boto3.resource('s3',aws_access_key_id="xxxxx",
         aws_secret_access_key= "xxxxx",config=Config(signature_version='s3v4'), region_name='ap-south-1')

    client = boto3.client('s3',aws_access_key_id="AKIASMSBDZXUPALNUHGN",
        aws_secret_access_key= "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",config=Config(signature_version='s3v4'), region_name='ap-south-1')

    for bucket in s3.buckets.all():
        pass

    filename = []
    fileurl = []

    for object in bucket.objects.all():
        filekey = object.key
        filename.append(filekey[19:])
        fileurl.append(client.generate_presigned_url('get_object', Params = {'Bucket':'dti-project','Key':filekey}, ExpiresIn = 600))
    
    return render(request, "dashboard.html",{'filename':filename , 'fileurl':fileurl})

