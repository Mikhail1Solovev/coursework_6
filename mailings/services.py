from datetime import datetime, timedelta
from django.conf import settings
from django.core.mail import send_mail
from .models import Mailing, MailingAttempt

def process_mailings():
    current_time = datetime.now()
    mailings = Mailing.objects.filter(start_datetime__lte=current_time, status='created')

    for mailing in mailings:
        for client in mailing.clients.all():
            try:
                send_mail(
                    subject=mailing.message.subject,
                    message=mailing.message.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email],
                    fail_silently=False,
                )
                MailingAttempt.objects.create(mailing=mailing, status='успешно')
            except Exception as e:
                MailingAttempt.objects.create(mailing=mailing, status='не успешно', response=str(e))

        mailing.status = 'completed'
        mailing.save()
