# automated_email/management/commands/send_test_email.py
from django.core.mail import send_mail
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Send a test email to verify the email setup'

    def handle(self, *args, **kwargs):
        send_mail(
            'Test Email',
            'This is a test email sent from Django.',
            'iamshanusinha@gmail.com',  # From email (use your actual email)
            ['thodomerai69@gmail.com'],  # Recipient email
            fail_silently=False,
        )
        self.stdout.write(self.style.SUCCESS('Test email sent successfully!'))