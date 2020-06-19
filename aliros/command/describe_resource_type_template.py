import json
from aliyunsdkros.request.v20150901.DescribeResourceTypeTemplateRequest import DescribeResourceTypeTemplateRequest


def add_command_arguments(parser):
    parser.add_argument('--type-name', metavar='string', required=True)


def execute(args, client):
    request = DescribeResourceTypeTemplateRequest()

    request.set_TypeName(args.type_name)

    status, headers, body = client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return 0
    else:
        raise Exception('Unexpected errors: status=%d, error=%s' % (status, body))
