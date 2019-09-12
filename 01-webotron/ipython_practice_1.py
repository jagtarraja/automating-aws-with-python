# coding: utf-8
import boto3
session = boto3.Session(profile_name='aws-access')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
ec2 = session.resource('ec2')
for instance in ec2.instance.all():
    print(instance)
    
new-bucket = s3.create_bucket(Bucket='navi_bucket)
new_bucket = s3.create_bucket('automatedbucket')
new_bucket = s3.create_bucket(Bucket='automatedbucket')
new_bucket = s3.create_bucket(Bucket='automatedbucketq')
for bucket in s3.buckets.all():
    print(bucket)
    
ec2_client = session.client('ec2')
ec2_client
ec2_client.allocate_address()
get_ipython().run_line_magic('history', '')
