import json
from aliros.template import Template_YAML
from aliros.stack import find_stack_id, send_request
from aliyunsdkros.request.v20150901.UpdateStackRequest import UpdateStackRequest


def add_command_arguments(parser):
    parser.add_argument('--stack-name', metavar='string', required=True, help='name of stack')
    parser.add_argument('--template-url', metavar='string', required=True, help='url of template file')
    parser.add_argument('--timeout-mins', metavar='int', required=False, default=60, help='timeout minutes')


def execute(args, client):
    template = Template_YAML()
    template.load(args.template_url)

    body = {
        'Template': json.dumps(template.content),
        'TimeoutMins': args.timeout_mins,
    }

    request = UpdateStackRequest()

    request.set_StackName(args.stack_name)
    request.set_StackId(find_stack_id(client, request))

    request.set_content(json.dumps(body))
    request.set_content_type('application/json')

    send_request(client, request)
