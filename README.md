                                     Coda integration

***
For run the project:
1. Clone the repository using `git clone`.
2. Set up a database in `PostgreSQL`.
3. Create a new file called `.env` in the project root and fill it as shown in `.env.example`.
4. Install the requirements `pip install -r requirements.txt`
5. Run `python manage.py migrate` in terminal.
6. Run `django-admin compilemessages` in terminal.
7. Run `python manage.py runserver` in terminal.
8. For Celery worker:
   * on Windows: 
       * use gevent task pool, run `pip install gevent`;
       * run in root `celery -A eai worker -l info -P gevent`;
    * on Unix:
       * run in root `celery -A eai worker -l info`;
       * 
***

**Facebook Webhook** endpoint checking includes request ips to FB ips range from `config/fb_ips.txt` in class `FacebookRequestValidator`. For update ips use `whois -h whois.radb.net -- '-i origin AS32934' | grep -Eo '([0-9a-f.:]+){1,}/[0-9]+'` in cmd, then put ipv4 and ipv6 addresses to file `config/fb_ips.txt`.
***
**For set up Selenium** you can set necessary browser ("FIREFOX", "CHROME", "UNDETECTABLE_CHROME") in `.env` `WEBDRIVER_BROWSER` param. Then for manual `chrome driver` set `WEBDRIVER_CHROME_PATH` or write installed chrome version in `CHROME_VERSION` for auto downloading. If you wanna Firefox, app support only manual install of `geckodriver`, and set `WEBDRIVER_FIREFOX_PATH`. For undetected chrome app support only manual install too, then set the `WEBDRIVER_CHROME_PATH`.

Headless mode controlling browser view, set `bool` in `WEBDRIVER_HEADLESS`. For imitate display set `VIRTUAL_DISPLAY_ENABLED`, it can be used if you employ server deployment.



