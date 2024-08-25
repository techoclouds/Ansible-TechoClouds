
from ansible.plugins.lookup import LookupBase
import boto3

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        region = terms[0]
        instance_state = kwargs.get('state', 'running')  # Default state is 'running'
        ec2 = boto3.client('ec2', region_name=region)

        response = ec2.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': [instance_state]}]
        )
        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append(instance['InstanceId'])

        return instances
