import boto3
import logging
from botocore.exceptions import ClientError
import json

# print(json.dumps(data, indent=2, default=str))


s3 = boto3.resource('s3')

def delete_bucket(bucket_name, region=None):
    # when all things are good - I need to take into account 1. Do I have a region location specified or not? Look in the default region, if not region specified
    # Once location is set, I need to grab a list of all the bucket names and then compare that to the bucket name that I have inputted for bucket name
    
    try:
        # Location is not provided
        # print('made it here')
        if region == None:
            # print('made it here again')
            s3_client = boto3.client('s3')
            # logic for deleting the bucket
            
            # first you have to list then delete bucket contents
            
            
            data = s3_client.list_objects_v2(
                Bucket=bucket_name
            )
            
            if data['KeyCount'] == 0:
                print('Keycount is zero')
                s3_client.delete_bucket(Bucket=bucket_name)
            else:
                contents = data['Contents']
                for object in contents:
                    s3_client.delete_object(Bucket=bucket_name, Key=object['Key'])
                    
                s3_client.delete_bucket(Bucket=bucket_name)
    except:
        print('that did not work')
        
        
delete_bucket('aeriels2')