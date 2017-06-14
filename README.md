# fcm-django-web-demo

Quick demo to demonstrate the use of firebase web push notifications with the use of `javascript` on frontend, `django` on backend and push notifications via `fcm-django` pypi package for django.
Supports HTTPS (useful if running demo on `localhost` is not an option).

## Quick start

### general
- in `fcm-django-web-demo`:
  - create virtual environment with `python -m virtualenv env` (or `python -m venv env` in Python 3)
  - activate virtual environment with `. env/bin/activate`
  - install necessary Python packages with `pip install -r requirements.txt`

### frontend
- in `fcm-django-web-demo`:
  - generate self-signed certificate and key with: `openssl req -nodes -new -x509 -keyout key.pem -out cert.pem`
- in `fcm-django-web-demo/frontend`:
  - change protocol to https (index.html, line 194)
  - run server with `python server.py`

### backend
- in `fcm-django-web-demo/mysite`:
  - run database migrations with `python manage.py migrate`
  - create Django administrator with `python manage.py createsuperuser`
  - collect static files with `python manage.py collectstatic`
  - add host IP address to ALLOWED_HOSTS in settings.py in mysite folder
  - run server with `python manage.py runsslserver --certificate ../cert.pem --key ../key.pem 0.0.0.0:8000`.

### how to use
- open https://0.0.0.0:4443 in your browser of choice and allow untrusted connection (run Chrome with --ignore-certificate-errors flag)
- request token and allow firebase to send notifications to your browser (device)
- you should now be seeing your instance id token on the aforementioned URL
- if you go to django admin, https://0.0.0.0:8000/admin/fcm_django/fcmdevice/ (allow untrusted connection again), you should be seeing a FCMDevice instance for your browser
- send yourself a test notification with django admin actions
  - shell example (run `python manage.py shell` from `fcm-django-web-demo/mysite`):
    ```python
	   from fcm_django.models import FCMDevice
	   devices = FCMDevice.objects.all()
	   devices[0].send_message(title='title', body='message')
    ```
- voila :)

### fcm-django API URL docs

  - available via `coreapi` and `djangorestframework` pypi packages, can be accessed at http://localhost:8000/docs

