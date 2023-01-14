import boto3
import os
from termcolor import colored

bucket_name = ''

def get_bucket_name():
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    for bucket in response['Buckets']:
        if "bucket-for-backuper-" in bucket['Name']:
            return bucket['Name']

def sync_with_s3():
    with open('paths_to_targets.txt') as file_with_targets:
        targets = file_with_targets.readlines() 
    bucket_name = get_bucket_name()
    print(colored("Backup was successfully started. Backing up to ", "green") + colored(bucket_name, "magenta"))
    for target_path in targets:
        os.system("aws s3 sync --delete " + target_path + " s3://" + bucket_name + target_path + "/")

sync_with_s3()