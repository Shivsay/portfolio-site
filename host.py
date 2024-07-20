import logging
import boto3
from botocore.exceptions import ClientError
import os
import json

def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    print("Creating Bucket")
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

    create_web_bucket(bucket_name,s3_client)
    print("Process Completed")
    return True

def create_web_bucket(bucket_name, s3_client):


    # Configure static hosting
    print("Configuring the static hosting")

    website_configuration = {
        'IndexDocument': {'Suffix': 'index.html'},
    }

    s3_client.put_bucket_website(Bucket=bucket_name, WebsiteConfiguration=website_configuration)

    # Uploading the files
    print("Uploading files")

    s3_client.upload_file('./index.html', bucket_name, 'index.html',ExtraArgs={'ContentType': 'text/html'})
    s3_client.upload_file('./styles.css', bucket_name, 'styles.css',ExtraArgs={'ContentType': 'text/css'})
    s3_client.upload_file('./assets/fact-checker.jpg', bucket_name, 'fact-checker.jpg',ExtraArgs={'ContentType': 'image/jpeg'})
    s3_client.upload_file('./assets/identity-logger.jpg', bucket_name, 'identity-logger.jpg',ExtraArgs={'ContentType': 'image/jpeg'})
    s3_client.upload_file('./assets/mypic.jpg', bucket_name, 'mypic.jpg',ExtraArgs={'ContentType': 'image/jpeg'})
    s3_client.upload_file('./assets/pyhack.png', bucket_name, 'pyhack.png',ExtraArgs={'ContentType': 'image/png'})
    s3_client.upload_file('./assets/rights-quest.png', bucket_name, 'rights-quest.png',ExtraArgs={'ContentType': 'image/png'})
    s3_client.upload_file('./assets/webpAIge.png', bucket_name, 'webpAIge.png',ExtraArgs={'ContentType': 'image/png'})

    # Configure the policy
    print("Setting policy")

    s3_client.delete_public_access_block(Bucket=bucket_name)

    bucket_policy = {
        "Id": "Policy1721458320283",
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "Stmt1721458317167",
              "Action": [
                "s3:GetObject"
              ],
              "Effect": "Allow",
              "Resource": f'arn:aws:s3:::{bucket_name}/*',
              "Principal": "*"
            }
          ]
    }
    # Convert the policy from JSON dict to string
    bucket_policy = json.dumps(bucket_policy)

    # Set the new policy
    s3_client.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)


success = create_bucket("say-portfolio-bucket")
