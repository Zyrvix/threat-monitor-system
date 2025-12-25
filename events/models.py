from django.db import models
from constants import SEVERITY_LEVELS, EVENT_TYPES

class Event(models.Model):
    source_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=100, choices=EVENT_TYPES)
    severity = models.CharField(max_length=20, choices=SEVERITY_LEVELS, db_index=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    ip_address = models.GenericIPAddressField(null=True, blank=True, db_index=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    isp = models.CharField(max_length=255, null=True, blank=True)
    asn = models.CharField(max_length=100, null=True, blank=True)
    is_proxy = models.BooleanField(default=False)
    is_vpn = models.BooleanField(default=False)

    device_type = models.CharField(max_length=50, null=True, blank=True)
    os_family = models.CharField(max_length=100, null=True, blank=True)
    os_version = models.CharField(max_length=100, null=True, blank=True)
    browser_family = models.CharField(max_length=100, null=True, blank=True)
    browser_version = models.CharField(max_length=100, null=True, blank=True)
    user_agent_string = models.TextField(null=True, blank=True)

    request_method = models.CharField(max_length=10, null=True, blank=True)
    request_path = models.CharField(max_length=255, null=True, blank=True)
    headers_dump = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.event_type} - {self.severity} ({self.source_name})"
