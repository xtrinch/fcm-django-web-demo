# fcm-django-web-demo

Quick demo to demonstrate the use of firebase web push notifications with the use of `javascript` on frontend, `django` on backend and push notifications via `fcm-django` pypi package for django.

## Quick start

### general
- in `fcm-django-web-demo`:
  - create virtual environment with `python -m virtualenv env` (or `python -m venv env` in Python 3)
  - activate virtual environment with `. env/bin/activate`
  - install necessary Python packages with `pip install -r mysite/requirements.txt`

### frontend (in `fcm-django-web-demo/frontend`)
- run server with `python -m SimpleHTTPServer 8001`

### backend
- in `fcm-django-web-demo/mysite`:
  - run database migrations with `python manage.py migrate`
  - create Django administrator with `python manage.py createsuperuser`
  - collect static files with `python manage.py collectstatic`
  - run server with `python manage.py runserver 0.0.0.0:8000`.

### how to use
- open http://localhost:8001 in your browser of choice
- request token and allow firebase to send notifications to your browser (device)
- you should now be seeing your instance id token on the aforementioned URL
- if you go to django admin, http://localhost:8000/admin/fcm_django/fcmdevice/, you should be seeing a FCMDevice instance for your browser
- send yourself a test notification with django admin actions
  - shell example (run `python manage.py shell` from `fcm-django-web-demo/mysite`):
    ```python
	   from fcm_django.models import FCMDevice
	   device = FCMDevice.objects.all().first()
	   device.send_message(title='title', body='message')
    ```
- voila :)

### fcm-django API URL docs

- available via `coreapi` and `djangorestframework` pypi packages, can be accessed at http://localhost:8000/docs

### short notes about how to run this demo with HTTPS support in case `localhost` is not an option
- generate certificate and key with `openssl req -nodes -new -x509 -keyout key.pem -out cert.pem` in `fcm-django-web-demo`
- in `fcm-django-web-demo/frontend`:
  - update URL protocol to `https` and `localhost` to your server's IP address in [index.html](https://github.com/Pymancer/fcm-django-web-demo/blob/3471b0be6a6f01c282d12924323556129b04b379/frontend/index.html#L194)
  - run frontend server with `python server.py` 
- in `fcm-django-web-demo/mysite`:
  - add your server's IP address to allowed hosts in project settings (shell example: `echo "ALLOWED_HOSTS = ['172.20.1.10']" > mysite/local_settings.py`)
  - run backend server with `python manage.py runsslserver --certificate ../cert.pem --key ../key.pem 0.0.0.0:8000`
- testing this demo in Chrome may require to run it with `--ignore-certificate-errors` flag to avoid SSL certificate fetch errors
- during the testing allow untrusted connections to the demo servers on browser prompt
