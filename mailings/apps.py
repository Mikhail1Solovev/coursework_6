from django.apps import AppConfig
from time import sleep

class MailingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailings'

    def ready(self):
        from .tasks import start
        sleep(2)
        start()
