from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

def send_signup_email(username):
    context = {
        'username': username
    }

    email_subject = 'New User registered!'
    email_body = render_to_string('email_message.txt', context)

    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, settings.DEFAULT_TO_EMAIL,
    )

    return email.send(fail_silently=False)