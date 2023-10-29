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
        # check if bucket even exists
        # Then list all the bucket contents
        # delete bucket contents
        # delete bucket
        
        
        s3_client = boto3.client('s3')
        all_buckets = s3_client.list_buckets()
        # print(all_buckets['Buckets'])
        
        buckets = all_buckets['Buckets']
        
        for bucket in buckets:
            data = s3_client.list_objects_v2(
                    Bucket=bucket_name
                )
            print(data[])
            print(len(data))
            if bucket_name in bucket['Name'] and len(data) > 0:               
                print('1')
                contents = data['Content']
                print(contents)
                
                print(json.dumps(contents, indent=2, default=str))
                # gave me a large dictionary, so I needed to use a forloop to get access to everything things
                
                for object in contents:
                    # print(object)
                    # print(bucket_name)
                    # print(object['Key'])
                    s3_client.delete_object(Bucket=bucket_name, Key=object['Key'])
                    
                # officially deleting the bucket
                print('2')
            else:
                print("bucket does not exist")        
    except:
        print('that did not work')
        
delete_bucket('aeriels')