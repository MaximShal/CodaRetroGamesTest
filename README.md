                                     Coda integration

***
For run the project:
1. Clone the repository using `git clone`.
2. Create a new file called `.env` in the project root and fill it as shown in `.env.example`.
3. Install the requirements `pip install -r requirements.txt`.
4. Run Celery worker:
   * on Windows: 
       * use gevent task pool, run `pip install gevent`;
       * run in root `celery -A celery_app worker -l info -P gevent`;
    * on Unix:
       * run in root `celery -A celery_app worker -l info`;
5. Run Celery Beat run in root `celery -A celery_app beat -l info`
***
