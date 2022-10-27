import boto3

def start_instance(id):
    client = boto3.client('ec2')
    response = client.start_instances(
        InstanceIds=[
            id,
        ],
    )
    print(response)

if __name__ == "__main__":
    start_instance("i-0a9e5646c62b4320c")