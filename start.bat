@echo off
call venv\Scripts\activate
start "Analyze Worker" /separate cmd /k "celery -A celery_app worker -l info -P gevent"


@echo off
call venv\Scripts\activate
start "Analyze Beat" /separate cmd /k "celery -A celery_app beat -l info"