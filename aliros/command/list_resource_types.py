import json
from aliyunsdkros.request.v20150901.DescribeResourceTypesRequest import DescribeResourceTypesRequest


def add_command_arguments(parser):
    parser.add_argument('--support-status', metavar='string', required=False)


def execute(args, client):
    request = DescribeResourceTypesRequest()
    args.support_status and request.set_SupportStatus(args.support_status)

    status, headers, body = client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return 0
    else:
        raise Exception('Unexpected errors: status=%d, error=%s' % (status, body))
