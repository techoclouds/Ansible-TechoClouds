
from ansible.plugins.lookup import LookupBase
import boto3

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        region = terms[0]  # AWS region is the first term
        ec2 = boto3.client('ec2', region_name=region)

        # Retrieve the list of instances
        response = ec2.describe_instances()
        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append(instance['InstanceId'])

        return instances
