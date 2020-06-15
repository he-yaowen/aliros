from aliros.stack import find_stack_id, send_request
from aliyunsdkros.request.v20150901.DeleteStackRequest import DeleteStackRequest


def add_command_arguments(parser):
    parser.add_argument('--stack-name', metavar='string', required=True)


def execute(args, client):
    request = DeleteStackRequest()

    request.set_StackName(args.stack_name)
    request.set_StackId(find_stack_id(client, args.stack_name))

    send_request(client, request)
