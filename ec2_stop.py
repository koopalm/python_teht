import boto3

def stop_instance(id):
    client = boto3.client('ec2')
    response = client.stop_instances(
        InstanceIds=[
            id,
        ],
    )
    print(response)

if __name__ == "__main__":
    stop_instance("i-0a9e5646c62b4320c")