import threading
from django.conf import settings
from accounts.tokens import generate_token
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        # super().__init__(self)
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=True)


def generate_email_message(user):
    # Extract the part before the "@" in the email
    name = user.email.split('@')[0]

    if user.role == "admin":
        return f"""
Hi {name},

Welcome to Etal Admin Platform! Your admin account is set up, and you're ready to manage the ecosystem. Please visit the admin url to gain access.

For any assistance, feel free to reach out. We're here to support you.

Best,
The Etal Team
"""

    elif user.role == "athlete":
        return f"""
Hi {name},

Welcome to Etal! Your account is now active, and you're all set to create you profile and interact with scouts in our ecosystem. Please verify your email to access all out platform features.

Need help? We're just a message away.

Best regards,
The Etal Team
"""

    elif user.role == "scout":
        return f"""
Hi {name},

Welcome to Etal! Your account is ready, and we're excited to have you as part of our network. Please verify your email to gain access to our pool of Talents.

For any queries, don't hesitate to contact us.

Best,
The Etal Team
"""


class EmailService:
    def send_welcome_email(self, user):
        subject = "Welcome to Etal, Your Scouting Platform!"
        message = generate_email_message(user)
        welcome_email = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        EmailThread(welcome_email).start()

    def send_account_verification_email(self, request, user):
        current_site = get_current_site(request)
        email_confirmation_subject = "Verify Your Email - Etal"
        email_confirmation_message = render_to_string('mail/email_confirmation.html', {
            'name': user.email.split('@')[0],
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        })

        email = EmailMessage(
            email_confirmation_subject,
            email_confirmation_message,
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        EmailThread(email).start()
