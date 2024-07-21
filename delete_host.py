import logging
import boto3
from botocore.exceptions import ClientError

def delete_all_objects(bucket_name,s3_client):
    # The Key field is for the name of the file
    s3_client.delete_objects(
        Bucket=bucket_name,
        Delete={
                'Objects': [
                    {
                        'Key': 'index.html',
                    },
                    {
                        'Key': 'styles.css',
                    },
                    {
                        'Key': 'fact-checker.jpg',
                    },
                    {
                        'Key': 'identity-logger.jpg',
                    },
                    {
                        'Key': 'mypic.jpg',
                    },
                    {
                        'Key': 'pyhack.png',
                    },
                    {
                        'Key': 'rights-quest.png',
                    },
                    {
                        'Key': 'webpAIge.png',
                    },
                ],
        }
    )

def delete_bucket(bucket_name, region=None):
    """Deleting an S3 bucket in a specified region

    If a region is not specified, the bucket is deleted in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket deleted, else False
    """

    print("Connecting...")
    try:
        if region is None:
            s3_client = boto3.client('s3')
        else:
            s3_client = boto3.client('s3', region_name=region)

    except ClientError as e:
        logging.error(e)
        return False
    
    print("Emptying contents")
    delete_all_objects(bucket_name,s3_client)
    
    print("Deleting bucket")
    s3_client.delete_bucket(Bucket=bucket_name)

    return True


# Add a bucket name and region here
success = delete_bucket("your bucket name here")
print("Success")
