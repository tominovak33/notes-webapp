import sendgrid
import os
from sendgrid.helpers.mail import *

import config

sg = sendgrid.SendGridAPIClient(apikey=config.SENDGRID_API_KEY)


def send_mail(to, subject, content, template_id=False):
    from_email = Email(config.SENDGRID_FROM_EMAIL_ADDRESS)

    to_email = Email(to)
    email_content = Content("text/html", content)
    mail = Mail(from_email, subject, to_email, email_content)
    if template_id:
        mail.set_template_id('06ac801d-a03f-4c1a-bec3-0a4d4ac6b867')
    response = sg.client.mail.send.post(request_body=mail.get())
    print response
    return response

# Example email sending
# Import mail
# mail.send_mail("destination@example.com", "My subject", "The test content", "06ac801d-a03f-4c1a-bec3-0a4d4ac6b867")

