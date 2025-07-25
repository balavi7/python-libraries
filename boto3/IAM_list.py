import boto3

iam = boto3.client('iam')
paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
    for user in response['Users']:
        print("User Name:", user['UserName'])
        print("User ID:", user['UserId'])