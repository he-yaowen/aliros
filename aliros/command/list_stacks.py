import json
from aliyunsdkros.request.v20150901.DescribeStacksRequest import DescribeStacksRequest


def add_command_arguments(parser):
    parser.add_argument('--stack-id', metavar='string', required=False)
    parser.add_argument('--name', metavar='string', required=False)
    parser.add_argument('--status', metavar='string', required=False)
    parser.add_argument('--page-number', metavar='int', required=False, default=1)
    parser.add_argument('--page-size', metavar='int', required=False, default=10)


def execute(args, client):
    request = DescribeStacksRequest()
    args.stack_id and request.set_StackId(args.stack_id)
    args.name and request.set_Name(args.name)
    args.status and request.set_Status(args.status)
    request.set_PageNumber(args.page_number)
    request.set_PageSize(args.page_size)

    status, headers, body = client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return 0
    else:
        raise Exception('Unexpected errors: status=%d, error=%s' % (status, body))
