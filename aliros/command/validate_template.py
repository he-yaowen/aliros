import json
from aliros.template import Template_YAML
from aliros.stack import send_request
from aliyunsdkros.request.v20150901.ValidateTemplateRequest import ValidateTemplateRequest


def add_command_arguments(parser):
    parser.add_argument('--template-url', metavar='string', required=True, help='url of template file')


def execute(args, client):
    template = Template_YAML()
    template.load(args.template_url)

    body = {
        'Template': json.dumps(template.content),
    }

    request = ValidateTemplateRequest()
    request.set_content(json.dumps(body))
    request.set_content_type('application/json')

    send_request(client, request)
