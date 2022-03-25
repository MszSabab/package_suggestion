from django.db import models

from django.utils import timezone
from django.db.models import JSONField


def default_info_field():
    return {
        "codes": [],
        "media": [],
    }


class Service(models.Model):
    id = models.CharField(max_length=30, blank=True, primary_key=True, default="")
    name = models.CharField(max_length=30, default=timezone.now, blank=True)
    price = models.CharField(max_length=30, default=timezone.now, blank=True)
    details = JSONField(null=False, blank=True, default=default_info_field)
    view_order = models.CharField(max_length=30, default=False)
    status = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
