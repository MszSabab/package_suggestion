from django.db import models

from django.utils import timezone
from django.db.models import JSONField


def default_info_field():
    return {
        "names": [],
    }


class Service(models.Model):
    names = JSONField(null=False, blank=True, default=default_info_field)
    total_price = models.CharField(max_length=30, blank=True)
    # details = JSONField(null=False, blank=True, default=default_info_field)
    # view_order = models.CharField(max_length=30, default=False)
    # status = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.names

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
