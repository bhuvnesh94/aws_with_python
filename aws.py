#!/usr/bin/python3

import boto3 #importing library

ec2=boto3.client('ec2')
response=ec2.describe_instances()
print(response)
