import json
import boto3

ec2 = boto3.resource('ec2', region_name = 'ap-southeast-2')
client = boto3.client('ec2')

filters = [{'Name':'tag:Name', 'Values':['*']}]
vpcs = list(ec2.vpcs.filter(Filters=filters))

for vpc in vpcs:
    response = client.describe_vpcs(
        VpcIds=[
            vpc.id,
        ]
    )
    print(json.dumps(response, sort_keys=True, indent=4))
