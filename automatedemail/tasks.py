from celery import shared_task
from django.core.mail import send_mail
from automatedemail.csv import get_email_ids_from_csv  
from .csv import log_email_status

@shared_task
def send_automated_email():
    # List of email IDs
    email_ids = get_email_ids_from_csv('emails.csv')

    subject = "Reminder: Reporting Time"
    message = """
        <p><strong>Dear Trainee,</strong></p>


        <p>This is a friendly reminder to ensure your presence at the office tomorrow by 10:00 AM.

        We are excited to have you with us and look forward to a productive day ahead.

        Should you have any questions or require additional information, please don’t hesitate to reach out.<p>

        
        <p><strong>Best regards,</strong><br>

        <p><strong>Shanu Sinha</strong><br>
        <strong>CEO</strong><br>
        <strong>Social Paanda</strong></p>
    """
    
    # Sending email to each email ID
    for email in email_ids:
        try:
            send_mail(
                subject,
                message,
                'your_email@example.com', 
                [email],
                fail_silently=False,
                html_message=message 
            )
            log_email_status('logs/email_log.csv', email, 'Sent')  # Log success status  # Log success status
        except Exception as e:
            log_email_status('logs/email_log.csv', email, f'Failed: {str(e)}')  # Log failure status  # Log failure status
            
    return "Email sent successfully."