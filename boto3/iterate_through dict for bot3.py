import json
l =[1,2,3,5,0]
print(l[0])
response = {
    'Buckets': [
        {
            'Name': 'string',
            'CreationDate': 'datetime(2015, 1, 1)'
        },
        {
            'Name' : 'demo_bucket'
        },
    ],
    'Owner': {
        'DisplayName': 'string',
        'ID': 'string'
    },
    'ContinuationToken': 'string'
}

names = [bucket["Name"] for bucket in response['Buckets']]

print(names)

response = {
    'Owner': {
        'DisplayName': 'string',
        'ID': 'string'
    },
    'Grants': [
        {
            'Grantee': {
                'DisplayName': 'string',
                'EmailAddress': 'string',
                'ID': 'string',
                'Type': 'CanonicalUser|AmazonCustomerByEmail|Group',
                'URI': 'string'
            },
            'Permission': 'FULL_CONTROL'
        },
        {
            'Grantee': {
                'DisplayName': 'string2',
                'EmailAddress': 'string',
                'ID': 'string',
                'Type': 'CanonicalUser|AmazonCustomerByEmail|Group',
                'URI': 'string'
            },
            'Permission': 'FULL_CONTROL'
        },
    ]
} 

print(response)
DisplayName = [Grant["Grantee"]['DisplayName'] for Grant in response['Grants']]
print(DisplayName)


resposne= {'Snapshots': [{'Description': '', 'Encrypted': False, 'OwnerId': '609316111350', 'Progress': '100%', 'SnapshotId': 'snap-0009ce4b6c3963fce', 'StartTime': 'datetime.datetime(2024, 9, 3, 15, 51, 17, 430000, tzinfo=tzutc())', 'State': 'completed', 'VolumeId': 'vol-03230c66c902596dd', 'VolumeSize': 1, 'StorageTier': 'standard'}], 'ResponseMetadata': {'RequestId': '6c4bee3a-de8b-4888-a5c9-2dfac1957844', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '6c4bee3a-de8b-4888-a5c9-2dfac1957844', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '563', 'date': 'Tue, 03 Sep 2024 15:54:35 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}

for snapshots in resposne["Snapshots"]:
    snapshots_id = snapshots["SnapshotId"]
    print(snapshots_id)
    volume_id = snapshots["VolumeId"]
    print(volume_id)


response = {
    'Reservations': [
        {
            'Groups': [
                {
                    'GroupName': 'string',
                    'GroupId': 'string'
                },
            ],
            'Instances': [
                {
                    'AmiLaunchIndex': 123,
                    'ImageId': 'string',
                    'InstanceId': 'string',
                    'InstanceType': 'a1.medium',
                    'KernelId': 'string',
                    'KeyName': 'string',
                    'LaunchTime': 'datetime(2015, 1, 1)',
                    'Monitoring': {
                        'State': 'disabled'
                    },
                    'Placement': {
                        'AvailabilityZone': 'string',
                        'Affinity': 'string',
                        'GroupName': 'string',
                        'PartitionNumber': 123,
                        'HostId': 'string',
                        'Tenancy': 'default',
                        'SpreadDomain': 'string',
                        'HostResourceGroupArn': 'string',
                        'GroupId': 'string'
                    },
                    'Platform': 'Windows',
                    'PrivateDnsName': 'string',
                    'PrivateIpAddress': 'string',
                    'ProductCodes': [
                        {
                            'ProductCodeId': 'string',
                            'ProductCodeType': 'devpay'
                        },
                    ],
                    'PublicDnsName': 'string',
                    'PublicIpAddress': 'string',
                    'RamdiskId': 'string',
                    'State': {
                        'Code': 123,
                        'Name': 'pending'
                    },
                    'StateTransitionReason': 'string',
                    'SubnetId': 'string',
                    'VpcId': 'string',
                    'Architecture': 'i386',
                    'BlockDeviceMappings': [
                        {
                            'DeviceName': 'string',
                            'Ebs': {
                                'AttachTime': 'datetime(2015, 1, 1)',
                                'DeleteOnTermination': True|False,
                                'Status': 'attaching',
                                'VolumeId': 'this is instnace volume id',
                                'AssociatedResource': 'string',
                                'VolumeOwnerId': 'string'
                            }
                        },
                    ],
                    'ClientToken': 'string',
                    'EbsOptimized': True,
                    'EnaSupport': True,
                    'Hypervisor': 'ovm',
                    'IamInstanceProfile': {
                        'Arn': 'string',
                        'Id': 'string'
                    },
                    'InstanceLifecycle': 'spot',
                    'ElasticGpuAssociations': [
                        {
                            'ElasticGpuId': 'string',
                            'ElasticGpuAssociationId': 'string',
                            'ElasticGpuAssociationState': 'string',
                            'ElasticGpuAssociationTime': 'string'
                        },
                    ],
                    'ElasticInferenceAcceleratorAssociations': [
                        {
                            'ElasticInferenceAcceleratorArn': 'string',
                            'ElasticInferenceAcceleratorAssociationId': 'string',
                            'ElasticInferenceAcceleratorAssociationState': 'string',
                            'ElasticInferenceAcceleratorAssociationTime': 'datetime(2015, 1, 1)'
                        },
                    ],
                    'NetworkInterfaces': [
                        {
                            'Association': {
                                'CarrierIp': 'string',
                                'CustomerOwnedIp': 'string',
                                'IpOwnerId': 'string',
                                'PublicDnsName': 'string',
                                'PublicIp': 'string'
                            },
                            'Attachment': {
                                'AttachTime': 'datetime(2015, 1, 1)',
                                'AttachmentId': 'string',
                                'DeleteOnTermination': True,
                                'DeviceIndex': 123,
                                'Status': 'attaching',
                                'NetworkCardIndex': 123,
                                'EnaSrdSpecification': {
                                    'EnaSrdEnabled': True,
                                    'EnaSrdUdpSpecification': {
                                        'EnaSrdUdpEnabled': True
                                    }
                                }
                            },
                            'Description': 'string',
                            'Groups': [
                                {
                                    'GroupName': 'string',
                                    'GroupId': 'string'
                                },
                            ],
                            'Ipv6Addresses': [
                                {
                                    'Ipv6Address': 'string',
                                    'IsPrimaryIpv6': True
                                },
                            ],
                            'MacAddress': 'string',
                            'NetworkInterfaceId': 'string',
                            'OwnerId': 'string',
                            'PrivateDnsName': 'string',
                            'PrivateIpAddress': 'string',
                            'PrivateIpAddresses': [
                                {
                                    'Association': {
                                        'CarrierIp': 'string',
                                        'CustomerOwnedIp': 'string',
                                        'IpOwnerId': 'string',
                                        'PublicDnsName': 'string',
                                        'PublicIp': 'string'
                                    },
                                    'Primary': True,
                                    'PrivateDnsName': 'string',
                                    'PrivateIpAddress': 'string'
                                },
                            ],
                            'SourceDestCheck': True,
                            'Status': 'available',
                            'SubnetId': 'string',
                            'VpcId': 'string',
                            'InterfaceType': 'string',
                            'Ipv4Prefixes': [
                                {
                                    'Ipv4Prefix': 'string'
                                },
                            ],
                            'Ipv6Prefixes': [
                                {
                                    'Ipv6Prefix': 'string'
                                },
                            ],
                            'ConnectionTrackingConfiguration': {
                                'TcpEstablishedTimeout': 123,
                                'UdpStreamTimeout': 123,
                                'UdpTimeout': 123
                            }
                        },
                    ],
                    'OutpostArn': 'string',
                    'RootDeviceName': 'string',
                    'RootDeviceType': 'ebs',
                    'SecurityGroups': [
                        {
                            'GroupName': 'string',
                            'GroupId': 'string'
                        },
                    ],
                    'SourceDestCheck': True,
                    'SpotInstanceRequestId': 'string',
                    'SriovNetSupport': 'string',
                    'StateReason': {
                        'Code': 'string',
                        'Message': 'string'
                    },
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'VirtualizationType': 'hvm',
                    'CpuOptions': {
                        'CoreCount': 123,
                        'ThreadsPerCore': 123,
                        'AmdSevSnp': 'enabled'
                    },
                    'CapacityReservationId': 'string',
                    'CapacityReservationSpecification': {
                        'CapacityReservationPreference': 'open',
                        'CapacityReservationTarget': {
                            'CapacityReservationId': 'string',
                            'CapacityReservationResourceGroupArn': 'string'
                        }
                    },
                    'HibernationOptions': {
                        'Configured': True
                    },
                    'Licenses': [
                        {
                            'LicenseConfigurationArn': 'string'
                        },
                    ],
                    'MetadataOptions': {
                        'State': 'pending',
                        'HttpTokens': 'optional',
                        'HttpPutResponseHopLimit': 123,
                        'HttpEndpoint': 'disabled',
                        'HttpProtocolIpv6': 'disabled',
                        'InstanceMetadataTags': 'disabled'
                    },
                    'EnclaveOptions': {
                        'Enabled': True
                    },
                    'BootMode': 'legacy-bios',
                    'PlatformDetails': 'string',
                    'UsageOperation': 'string',
                    'UsageOperationUpdateTime': 'datetime(2015, 1, 1)',
                    'PrivateDnsNameOptions': {
                        'HostnameType': 'ip-name',
                        'EnableResourceNameDnsARecord': True,
                        'EnableResourceNameDnsAAAARecord': True
                    },
                    'Ipv6Address': 'string',
                    'TpmSupport': 'string',
                    'MaintenanceOptions': {
                        'AutoRecovery': 'disabled'
                    },
                    'CurrentInstanceBootMode': 'legacy-bios'
                },
            ],
            'OwnerId': 'string',
            'RequesterId': 'string',
            'ReservationId': 'string'
        },
    ],
    'NextToken': 'string'
}

volumeID_instnaces = [reservations["Instances"][0]["BlockDeviceMappings"][0]["Ebs"]['VolumeId'] for reservations in response["Reservations"]]

print("new volume id list is", volumeID_instnaces)
for reservations in response["Reservations"]:
    volume_id=reservations["Instances"][0]["BlockDeviceMappings"][0]["Ebs"]['VolumeId']
    print("instnace attached volume id is: ", volume_id)