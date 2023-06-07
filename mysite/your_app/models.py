import uuid
from django.db import models
from fcm_django.models import AbstractFCMDevice


class CustomDevice(AbstractFCMDevice, models.Model):
    # fields could be overwritten
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # could be added new fields
    updated_at = models.DateTimeField(auto_now=True)
