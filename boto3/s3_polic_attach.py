import boto3

s3 = boto3.client("s3")
bucket = s3.create_bucket(Bucket= "demo-chaitany305-bucket", CreateBucketConfiguration = {'LocationConstraint': 'eu-east-1'})

list_bucket = s3.list_buckets()


for buckets in list_bucket['Buckets']:
    bucket_name = buckets['Name']
    block_public_acess= s3.delete_public_access_block(Bucket = bucket_name)
    bucket_policy = s3.put_bucket_policy(
    Bucket= bucket_name,
    Policy=f'{{"Version": "2012-10-17", "Statement": [{{ "Sid": "id-1","Effect": "Allow","Principal": "*", "Action": [ "s3:PutObject"], "Resource": ["arn:aws:s3:::{bucket_name}/*"] }} ]}}',)