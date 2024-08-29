from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import Mailing, MailingAttempt


def send_mailing(mailing):
    recipients = [client.email for client in mailing.clients.all()]
    try:
        send_mail(
            subject=mailing.message.subject,
            message=mailing.message.body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipients,
            fail_silently=False,
        )
        MailingAttempt.objects.create(mailing=mailing, status='success', server_response='Success')
        mailing.status = 'completed'
        mailing.save()
    except Exception as e:
        MailingAttempt.objects.create(mailing=mailing, status='failure', server_response=str(e))


def process_mailings():
    current_time = timezone.now()
    mailings = Mailing.objects.filter(start_datetime__lte=current_time, status='created')

    for mailing in mailings:
        send_mailing(mailing)
