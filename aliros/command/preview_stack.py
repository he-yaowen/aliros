import json
from aliros.stack import send_request
from aliros.template import Template_YAML
from aliyunsdkros.request.v20150901.PreviewStackRequest import PreviewStackRequest


def add_command_arguments(parser):
    parser.add_argument('--stack-name', metavar='string', required=True, help='name of stack')
    parser.add_argument('--template-url', metavar='string', required=True, help='url of template file')
    parser.add_argument('--timeout-mins', metavar='int', required=False, default=60, help='timeout mintues')
    parser.add_argument('--disable-rollback', required=False, default=False, action='store_true',
                        help='disable rollback on failure')
    parser.add_argument('--parameters-url', metavar='string', required=False, help='url of file with parameters')


def execute(args, client):
    template = Template_YAML()
    template.load(args.template_url)

    body = {
        'Name': args.stack_name,
        'Template': json.dumps(template.content),
        'TimeoutMins': args.timeout_mins,
        'DisableRollback': args.disable_rollback
    }

    if args.parameters_url is not None:
        parameters = Template_YAML()
        parameters.load(args.parameters_url)
        body['Parameters'] = parameters.content

    request = PreviewStackRequest()
    request.set_content(json.dumps(body))
    request.set_content_type('application/json')

    send_request(client, request)
