from celery import Celery
from celery.schedules import crontab
from settings import CELERY_BROKER_URL

celery_app = Celery(
    'tasks',
    broker=CELERY_BROKER_URL,
    backend='rpc://'
)

celery_app.conf.beat_schedule = {
    'get_data_every_24h': {
        'task': 'tasks.get_coda_data',
        'schedule': crontab(hour='0', minute='0'),
    },
}
celery_app.conf.timezone = 'UTC'
