import boto3

ec2 = boto3.client("ec2")
#script to stop the runnig instnace only which has tag of ENV="dev"

#list the instnace which are currently running
instances = ec2.describe_instances(Filters = [{'Name': 'instance-state-name', 'Values': ['running']},{'Name': 'tag:ENV', 'Values': ['dev']}] )

instnaces_IDs = [instance['InstanceId'] for reservations in instances['Reservations'] for instance in reservations['Instances']] 


print('instance id are',instnaces_IDs)
#Now stop these instances
stop_instances = ec2.stop_instances( InstanceIds = instnaces_IDs)

print(stop_instances)
