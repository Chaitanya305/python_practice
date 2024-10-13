import boto3 

#list the EBS Snapshots we have
ec2 = boto3.client('ec2')
response= ec2.describe_snapshots(OwnerIds=["self"])

'''#list the ec2 instnaces and its volume asspociated list
response_instnace = ec2.describe_instances(Filters = [{'Name': 'instance-state-name' , 'Values': ['running', 'stopped', 'stopping']}])
volumeID_instnaces = []
for reservations in response_instnace["Reservations"]:
    try:
        volumeID_instnaces.append(reservations["Instances"][0]["BlockDeviceMappings"][0]["Ebs"]['VolumeId'])
    except:
        volumeID_instnaces.append("")
print(f'this is instnace associated volumes : {volumeID_instnaces}')
'''

for snapshots in response["Snapshots"]:
    volume_id = snapshots["VolumeId"]
    snapshots_id = snapshots["SnapshotId"]
    # will check the voulme id of snapshot if it is not present in volume_id_instnace.
    print(f'volume form which snapsot is craeted : {volume_id}')
    try:
        volume_response = ec2.describe_volumes(VolumeIds = [volume_id] )
        if not volume_response['Volumes'][0]['Attachments']:
            #as snapshot volume id from which this snapshot is created its volume is not attachec to any running or stop instance so delete it.
            del_snapshot = ec2.delete_snapshot(SnapshotId = snapshots_id)
            print(f"{snapshots_id} is deleted becouse volume is not attached to instnace")
       
    except ec2.exceptions.ClientError as e:
        #will check volume from which snapshot is created that volume itself not exist.
        if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
            del_snapshot = ec2.delete_snapshot(SnapshotId = snapshots_id)
            print(f"{snapshots_id} is deleted becouse volume is not exist") 
        
    

        
