from __future__ import print_function
import boto3
import traceback
from botocore.exceptions import ClientError

region = 'us-west-2'
WLisntances = ['i-xxxinstacenid','i-0xxxx']

def lambda_handler(event, context):
    try:
        ec2 = boto3.resource('ec2', region_name=region)
        client = boto3.client('ec2', region_name=region)
        for instance in ec2.instances.all():
            if instance.id in WLisntances:
                #statuss = client.start_instances(InstanceIds=[instance.id])
                print ("White listed Instance NOT going to shutdown" , instance.id)
            else:
                statuss = client.stop_instances(InstanceIds=[instance.id])
                print ("Instance going to Showdown",instance.id , instance.state)
    except:
        print('Failed! Debug further.')
        traceback.print_exc()

if __name__ == '__main__':
    lambda_handler('event', 'handler')
