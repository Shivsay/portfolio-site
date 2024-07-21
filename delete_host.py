import logging
import boto3
from botocore.exceptions import ClientError

def delete_all_objects(bucket_name,s3_client):
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

    print("Connecting...")
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

    except ClientError as e:
        logging.error(e)
        return False
    
    print("Emptying contents")
    delete_all_objects(bucket_name,s3_client)
    
    print("Deleting bucket")
    s3_client.delete_bucket(Bucket=bucket_name)

    return True


success = delete_bucket("say-portfolio-bucket")
print("Success")
