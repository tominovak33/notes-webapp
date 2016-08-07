import sendgrid
import os
from sendgrid.helpers.mail import *

import config

sg = sendgrid.SendGridAPIClient(apikey=config.SENDGRID_API_KEY)


def send_mail(to, subject, content):
    from_email = Email(config.SENDGRID_FROM_EMAIL_ADDRESS)

    to_email = Email(to)
    email_content = Content("text/plain", content)
    mail = Mail(from_email, subject, to_email, email_content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return response

# Example email sending
# Import mail
# mail.send_mail("destination@example.com", "My test email subject", "The test email content")

