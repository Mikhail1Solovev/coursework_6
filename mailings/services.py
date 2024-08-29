from django.utils import timezone
from .models import Mailing, MailingAttempt
from django.core.mail import send_mail
from django.conf import settings
import smtplib


def process_mailings():
    """
    Основная функция для обработки рассылок.
    Выбирает все активные рассылки и проверяет, нужно ли отправить сообщение.
    """
    now = timezone.now()
    active_mailings = Mailing.objects.filter(start_datetime__lte=now, status='active')

    for mailing in active_mailings:
        last_attempt = MailingAttempt.objects.filter(mailing=mailing).order_by('-attempt_datetime').first()

        if last_attempt:
            time_since_last_attempt = now - last_attempt.attempt_datetime
            if not should_send_now(mailing, time_since_last_attempt):
                continue

        try:
            send_mailing(mailing)
            mailing.status = 'completed'
            mailing.save()
        except smtplib.SMTPException as e:
            MailingAttempt.objects.create(mailing=mailing, status='failed', response=str(e))
        else:
            MailingAttempt.objects.create(mailing=mailing, status='success', response="Mail sent successfully")


def should_send_now(mailing, time_since_last_attempt):
    """
    Проверяет, нужно ли отправить сообщение в зависимости от периодичности рассылки.
    """
    if mailing.periodicity == 'daily' and time_since_last_attempt.days >= 1:
        return True
    elif mailing.periodicity == 'weekly' and time_since_last_attempt.days >= 7:
        return True
    elif mailing.periodicity == 'monthly' and time_since_last_attempt.days >= 30:
        return True
    return False


def send_mailing(mailing):
    """
    Отправляет email по указанным параметрам рассылки.
    """
    subject = mailing.message.subject
    message = mailing.message.body
    recipient_list = [client.email for client in mailing.clients.all()]

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list,
        fail_silently=False,
    )
