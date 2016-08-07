import sendgrid
import os
from sendgrid.helpers.mail import *

import config

# template_name: template_id
# template_name is for python code only, template_id is set in sendgrid
email_templates = {
    'test_template': '06ac801d-a03f-4c1a-bec3-0a4d4ac6b867',
}

sg = sendgrid.SendGridAPIClient(apikey=config.SENDGRID_API_KEY)


def send_mail(to, subject, content, template_name=False):
    from_email = Email(config.SENDGRID_FROM_EMAIL_ADDRESS)

    to_email = Email(to)
    email_content = Content("text/html", content)
    mail = Mail(from_email, subject, to_email, email_content)
    if template_name:
        mail.set_template_id(email_templates.get(template_name))
    response = sg.client.mail.send.post(request_body=mail.get())
    return response

# Example email sending
# Import mail
# mail.send_mail("destination@example.com", "My subject", "The test content", "test_template")
# ^ where 'test-template' is in the email_templates above
