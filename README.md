# Portfolio hosting

A simple portfolio website created using HTML and CSS (Bootstrap) with two scripts for hosting and deleting the website on an AWS S3 Bucket.

## Requirements

You need [python](https://www.python.org/downloads/), [aws cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and the [boto3](https://pypi.org/project/boto3/) SDK to run the scripts.

## Permissions

To use the script the user requires the permissions related to S3 bucket such as:

- For uploading the website:
    - PutBucketPolicy
    - PutBucketPublicAccessBlock

- For deleting the website:
    - DeleteBucket
    - DeleteObject

## Using the scripts

In both scripts, you need to manually add the bucket name and region.

For the `host.py` script you have to add both of the fields in the `create_bucket` function.

For the `delete_host.py` you have to add both of the fields in the `delete_bucket` function.

To call the scripts, use the following commands:
- `python host.py`
- `python delete_host.py`

To get the endpoint open the AWS S3 console, go to `Properties` tab in your bucket, scroll to the bottom and find the `Static Website hosting` section to get the url.

## Updation guide

In both the scripts the file's are added individually. If you need to add other resources, you'll need to modify the script accordingly.

AWS S3 buckets do support linking to directories. This issue is addressed in the HTML file using the [onerror](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#image_loading_errors) event handler, which points to the current directory if the required directories are missing.
