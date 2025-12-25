from django.db.models.signals import post_save
from django.dispatch import receiver
from events.models import Event
from .models import Alert
import logging

logger = logging.getLogger('security')

@receiver(post_save, sender=Event)
def auto_generate_alert(sender, instance, created, **kwargs):
    if created and instance.severity in ['high', 'critical']:
        alert = Alert.objects.create(
            event=instance,
            status='open'
        )
        logger.warning(f"ALERT_GENERATED: Automated alert {alert.id} created for {instance.event_type} "
                       f"(Severity: {instance.severity})")
