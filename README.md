# fcm-django-web-demo

Quick demo to demonstrate the use of firebase web push notifications with the use of `javascript` on frontend, `django` on backend and push notifications via `fcm-django` pypi package for django.
Python3 compatible only!

## Quick start

### prerequisites
- install python 3, pip
- in `fcm-django-web-demo`:
  - create virtual environment with `python -m venv env`
  - activate virtual environment with `source env/bin/activate` or `.\env\Scripts\activate.ps1` for Windows' Powershell
  - install necessary Python packages with `pip install -r mysite/requirements.txt`

### frontend
- in `fcm-django-web-demo/frontend`:
  - run server with `python -m http.server 8001`

### backend
- in `fcm-django-web-demo/mysite`:
  - run database migrations with `python manage.py migrate`
  - create Django administrator with `python manage.py createsuperuser`
  - collect static files with `python manage.py collectstatic`
  - run server with `python manage.py runserver 0.0.0.0:8000`.

### how to use
- open http://localhost:8001 in your browser of choice
- request token and allow firebase to send notifications to your browser (device) - if notifications are already allowed, there will only be a token displayed
- you should now be seeing your instance id token on the aforementioned URL
- if you go to django admin, http://localhost:8000/admin/fcm_django/fcmdevice/ and login with the superuser you created earlier, you should be seeing a FCMDevice instance for your browser
- send yourself a test notification with django admin actions OR
- send yourself notifications from the shell
    - example (run `python manage.py shell` from `fcm-django-web-demo/mysite`):
    ```python
	   from firebase_admin.messaging import Message, Notification
	   from fcm_django.models import FCMDevice
	   device = FCMDevice.objects.all().first()
	   device.send_message(Message(notification=Notification(title='title', body='message')))
    ```
- voila :)

### optional HTTPS support
- *why would you want to do this?* because service workers will not work on http, unless you are running them on localhost
- generate certificate and key with `openssl req -nodes -new -x509 -keyout key.pem -out cert.pem` in `fcm-django-web-demo`
- in `fcm-django-web-demo/frontend`:
  - update URL protocol to `https` and `localhost` to your server's IP address in [index.html](https://github.com/xtrinch/fcm-django-web-demo/blob/b8d552830de2b5d82e2d3f787e98d160160c0844/frontend/index.html#L194)
  - run frontend server with `python server.py` 
- in `fcm-django-web-demo/mysite`:
  - add your server's IP address to allowed hosts in project settings (shell example: `echo "ALLOWED_HOSTS = ['172.20.1.10']" > mysite/local_settings.py`)
  - run backend server with `python manage.py runsslserver --certificate ../cert.pem --key ../key.pem 0.0.0.0:8000`
- testing this demo in Chrome may require to run it with `--ignore-certificate-errors` flag to avoid SSL certificate fetch errors
- during the testing allow untrusted connections to the demo servers on browser prompt

### fcm-django DRF API URL docs demo

- available via `coreapi` and `djangorestframework` pypi packages, can be accessed at http://localhost:8000/docs
