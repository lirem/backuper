import logging
import boto3
import random
import string
from termcolor import colored


def create_new_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).
    """
    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def get_random_string():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    return result_str

def create_new_bucket_if_not_exist():
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    for bucket in response['Buckets']:
        if "bucket-for-backuper-" in bucket['Name']:
            print(colored("Bucket for Backuper exist.", "green"))
            return True
    
    added_string = get_random_string()
    bucket_name = f"bucket-for-backuper-{added_string}"
    print(colored(f"Bucket for Backuper doesn't exist, creating new one with a name{bucket_name}", "yellow"))

    s3.create_bucket(
        Bucket = bucket_name, 
        CreateBucketConfiguration={
        'LocationConstraint':'eu-central-1'
        },
        ACL="bucket-owner-full-control"
    )
    s3.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
        'BlockPublicAcls': True,
        'IgnorePublicAcls': True,
        'BlockPublicPolicy': True,
        'RestrictPublicBuckets': True
        }
    )

create_new_bucket_if_not_exist()