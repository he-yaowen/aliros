import json
from aliyunsdkros.request.v20150901.DescribeEventsRequest import DescribeEventsRequest
from aliyunsdkros.request.v20150901.DescribeStacksRequest import DescribeStacksRequest


def add_command_arguments(parser):
    parser.add_argument('--stack-name', metavar='string', required=True)
    parser.add_argument('--resource-status', metavar='string', required=False)
    parser.add_argument('--resource-name', metavar='string', required=False)
    parser.add_argument('--resource-type', metavar='string', required=False)
    parser.add_argument('--page-number', metavar='int', required=False, default=1)
    parser.add_argument('--page-size', metavar='int', required=False, default=10)


def execute(args, client):
    request = DescribeStacksRequest()
    request.set_Name(args.stack_name)
    status, headers, body = client.get_response(request)
    response = json.loads(body)

    if response['TotalCount'] != 1:
        raise Exception('Stacks with name "%s" not unique.' % args.stack_name)

    stack_id = response['Stacks'][0]['Id']

    request = DescribeEventsRequest()

    request.set_StackName(args.stack_name)
    request.set_StackId(stack_id)

    args.resource_status and request.set_ResourceStatus(args.resource_status)
    args.resource_name and request.set_ResourceName(args.resource_status)
    args.resource_type and request.set_ResourceType(args.resource_status)
    request.set_PageNumber(args.page_number)
    request.set_PageSize(args.page_size)

    status, headers, body = client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return 0
    else:
        raise Exception('Unexpected errors: status=%d, error=%s' % (status, body))
