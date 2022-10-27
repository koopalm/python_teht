import boto3

def create_security_group(from_port, to_port, cidr_block, name, description):
    ec2 = boto3.client('ec2')
    securitygroup = ec2.create_security_group(GroupName=name, Description=description)
    securitygroup.authorize_security_group_ingress(CidrIp=cidr_block, FromPort=from_port, ToPort=to_port, IpProtocol='tcp')


if __name__ == "__main__":
    create_security_group("22", "22", "0.0.0.0/0", "katri_boto", "allow ssh only")
