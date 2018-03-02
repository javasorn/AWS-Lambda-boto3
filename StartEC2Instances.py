import boto3

# Enter the region your instances are in, e.g. 'us-east-1'

region = 'ap-southeast-1'

# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']

instances = ['i-xxxxxx']



def lambda_handler(event, context):

    ec2 = boto3.client('ec2', region_name=region)

    ec2.start_instances(InstanceIds=instances)

    print 'stopped your instances: ' + str(instances)