# fcm-django-web-demo

Quick demo to demonstrate the use of firebase web push notifications with the use of `javascript` on frontend, `django` on backend and push notifications via `fcm-django` pypi package for django.

## Quick start

### frontend
  - run with `python -m SimpleHTTPServer 8001` in `fcm-django-web-demo/frontend`

### backend
  - run with `python manage.py migrate && python manage.py collectstatic` in `fcm-django-web-demo/mysite`
  - run with `python manage.py runserver 0.0.0.0:8000`.

### how to use
  - open http://localhost:8001 in your browser of choice and allow firebase to send notifications to it
  - you should now be seeing your instance id token on the forementioned URL
  - if you go to django admin, http://localhost:8000/admin/fcm_django, you should be seeing a FCMDevice instance for your browser
  - send yourself a test notification with django admin actions
  - voila :)

## fcm-django API URL docs

  - available via `coreapi` and `djangorestframework` pypi packages, can be accessed at http://localhost:8000/docs
