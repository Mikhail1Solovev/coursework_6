from apscheduler.schedulers.background import BackgroundScheduler
from .services import process_mailings

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(process_mailings, 'interval', minutes=1)
    scheduler.start()
