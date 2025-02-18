from celery_config import celery_app
from coda import Wrapper, settings
from pprint import pprint


wrapper = Wrapper(settings.CODA_DOC_ID, settings.CODA_TABLE_ID)


@celery_app.task
def get_coda_data():
    pprint(wrapper.get_list())
