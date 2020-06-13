import json
from aliyunsdkros.request.v20150901.DescribeStacksRequest import DescribeStacksRequest


def find_stack_id(client, stack_name):
    request = DescribeStacksRequest()
    request.set_Name(stack_name)
    status, headers, body = client.get_response(request)
    response = json.loads(body)

    if response['TotalCount'] > 1:
        raise Exception('Multiple stacks found with name "%s".' % stack_name)

    if response['TotalCount'] == 0:
        raise Exception('Stack with name "%s" not found.' % stack_name)

    return response['Stacks'][0]['Id']


def send_request(client, request):
    status, headers, body = client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return 0
    else:
        raise Exception('Unexpected errors: status=%d, error=%s' % (status, body))
