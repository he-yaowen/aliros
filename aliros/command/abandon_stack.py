from aliros.stack import find_stack_id, send_request
from aliyunsdkros.request.v20150901.AbandonStackRequest import AbandonStackRequest


def add_command_arguments(parser):
    parser.add_argument('--stack-name', metavar='string', required=True, help='name of stack')


def execute(args, client):
    request = AbandonStackRequest()

    request.set_StackName(args.stack_name)
    request.set_StackId(find_stack_id(client, args.stack_name))

    send_request(request)
