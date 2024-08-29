from apscheduler.schedulers.background import BackgroundScheduler
from .services import process_mailings

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(process_mailings, 'interval', seconds=10)
    scheduler.start()
