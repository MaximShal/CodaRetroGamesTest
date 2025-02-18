from environs import Env
from pathlib import Path

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent

CODA_API_TOKEN = env.str('CODA_API_TOKEN')
CODA_DOC_ID = env.str('CODA_DOC_ID')
CODA_TABLE_ID = env.str('CODA_TABLE_ID')

CELERY_BROKER_URL = env.str('CELERY_BROKER_URL')
