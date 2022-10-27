import boto3
from botocore.exceptions import ClientError

 
def delete_bucket(bucket_name):
    try:
        s3 = boto3.resource('s3')
        s3_bucket = s3.Bucket(bucket_name)
        bucket_versioning = s3.BucketVersioning(bucket_name)
        if bucket_versioning.status == 'Enabled':
            s3_bucket.object_versions.delete()
        else:
            s3_bucket.objects.all().delete()
            s3_bucket.delete()
        print("S3 bucket deleted successfully!")
    except ClientError as e:
        print(e)
 
if __name__ == "__main__":
    delete_bucket("katri-boto3-s3")
