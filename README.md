# fcm-django-web-demo

Quick demo to demonstrate the use of firebase web push notifications with the use of `javascript` on frontend, `django` on backend and push notifications via `fcm-django` pypi package for django.

## Quick start

### frontend
  - run with `python -m SimpleHTTPServer 8001` and use firefox (Couldn't get it to work in chrome and did not figure out why).

### backend
  - `python manage.py migrate && python manage.py collectstatic`
  - run with `python manage.py runserver 0.0.0.0:8000`.
