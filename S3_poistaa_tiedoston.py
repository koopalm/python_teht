import boto3


def delete_file(bucket, file_name):
    client = boto3.client('s3')
    client.delete_object(Bucket=bucket, Key=file_name)


if __name__ == "__main__":
    delete_file("katri-boto3-s3", "harj4.txt")
