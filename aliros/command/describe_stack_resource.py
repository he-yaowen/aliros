import json
from aliyunsdkros.request.v20150901.DescribeResourceDetailRequest import DescribeResourceDetailRequest
from aliyunsdkros.request.v20150901.DescribeStacksRequest import DescribeStacksRequest


def add_command_arguments(parser):
    parser.add_argument('--stack-name', metavar='string', required=True)
    parser.add_argument('--resource-name', metavar='string', required=True)


def execute(args, client):
    request = DescribeStacksRequest()
    request.set_Name(args.stack_name)
    status, headers, body = client.get_response(request)
    response = json.loads(body)

    if response['TotalCount'] != 1:
        raise Exception('Stacks with name "%s" not unique.' % args.stack_name)

    stack_id = response['Stacks'][0]['Id']

    request = DescribeResourceDetailRequest()

    request.set_StackName(args.stack_name)
    request.set_StackId(stack_id)
    request.set_ResourceName(args.resource_name)

    status, headers, body = client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return 0
    else:
        raise Exception('Unexpected errors: status=%d, error=%s' % (status, body))
