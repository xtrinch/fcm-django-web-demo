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
	   devices = FCMDevice.objects.all()
	   devices[0].send_message(title='title', body='message')
    ```
- voila :)

### fcm-django API URL docs

  - available via `coreapi` and `djangorestframework` pypi packages, can be accessed at http://localhost:8000/docs

