from django.db import models
from django.db.models import JSONField
from django.utils import timezone


def default_info_field():
    return {
        "codes": [],
        "media": [],
    }


class Package(models.Model):
    id = models.CharField(max_length=30, blank=True, primary_key=True, default="")
    name = models.CharField(max_length=30, default=timezone.now, blank=True)
    price = models.CharField(max_length=30, default=timezone.now, blank=True)
    details = JSONField(null=False, blank=True, default=default_info_field)
    service_ids = models.JSONField(null=False, blank=True, default=default_info_field)
    status = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
