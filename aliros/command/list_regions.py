import json
from aliyunsdkros.request.v20150901.DescribeRegionsRequest import DescribeRegionsRequest


def add_command_arguments(parser):
    pass


def execute(args, client):
    request = DescribeRegionsRequest()

    status, headers, body = client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return 0
    else:
        raise Exception('Unexpected errors: status=%d, error=%s' % (status, body))
