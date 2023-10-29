# create a s3 bucket
import boto3
import logging
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')
# describe which resource you are trying to work this

def create_bucket(bucket_name, region_name):
    try:
        if region_name == None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name)
            location = {'LocationConstraint': region_name}
            print('made it here')
            print(location)
            # {'LocationConstraint': 'us-east-1'}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
            print('created bucket')
    except ClientError as e:
        print('error')
        logging.error(e)
        return False
    return True
            
            


# create_bucket('aeriels2')
create_bucket('aeriels6thbucket', region_name='us-east-2')