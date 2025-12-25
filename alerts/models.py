from django.db import models
from django.conf import settings
from constants import ALERT_STATUS

class Alert(models.Model):
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, related_name='alerts')
    status = models.CharField(max_length=20, choices=ALERT_STATUS, default='open', db_index=True)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='assigned_alerts'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolution_notes = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Alert for {self.event.event_type} - {self.status}"
