from django.test import TestCase
from events.models import Event
from alerts.models import Alert
from django.contrib.auth import get_user_model

User = get_user_model()

class AlertAutomationTests(TestCase):
    def test_high_severity_creates_alert(self):
        Event.objects.create(
            source_name="Sensor-A",
            event_type="malware",
            severity="high",
            description="Trojan detected"
        )
        
        self.assertEqual(Alert.objects.count(), 1)
        alert = Alert.objects.first()
        self.assertEqual(alert.event.severity, "high")
        self.assertEqual(alert.status, "open")

    def test_low_severity_no_alert(self):
        Event.objects.create(
            source_name="Sensor-B",
            event_type="login_fail",
            severity="low",
            description="Minor issue"
        )
        
        self.assertEqual(Alert.objects.count(), 0)
