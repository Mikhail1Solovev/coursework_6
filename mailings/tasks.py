from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz
from django.core.mail import send_mail
from django.conf import settings
from .models import Mailing, MailingAttempt


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(process_mailings, 'interval', minutes=1)
    scheduler.start()


def process_mailings():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_time = datetime.now(zone)

    mailings = Mailing.objects.filter(start_datetime__lte=current_time, status='created')

    for mailing in mailings:
        clients = mailing.clients.all()
        for client in clients:
            try:
                send_mail(
                    subject=mailing.message.subject,
                    message=mailing.message.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email],
                    fail_silently=False,
                )
                # Логирование успешной попытки
                MailingAttempt.objects.create(
                    mailing=mailing,
                    timestamp=current_time,
                    status='success',
                    response='Mail sent successfully'
                )
            except Exception as e:
                # Логирование неудачной попытки
                MailingAttempt.objects.create(
                    mailing=mailing,
                    timestamp=current_time,
                    status='failed',
                    response=str(e)
                )
        # Обновление статуса рассылки после обработки всех клиентов
        mailing.status = 'completed'
        mailing.save()


# Функция, которая должна быть импортирована
def start():
    start_scheduler()
