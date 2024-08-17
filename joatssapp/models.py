from django_extensions.db.models import TimeStampedModel

from django.db import models


class Traffic(TimeStampedModel):
    ip = models.CharField(verbose_name="방문자 ip", max_length=127)
