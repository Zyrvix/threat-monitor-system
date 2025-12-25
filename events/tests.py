from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Event
from django.contrib.auth import get_user_model
from constants import EVENT_TYPES, SEVERITY_LEVELS

User = get_user_model()

class EventIngestionTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="password123")
        self.client.force_authenticate(user=self.user)

    def test_ingest_event_with_enrichment(self):
        url = reverse('events-ingest')
        data = {
            "source_name": "Firewall-01",
            "event_type": "intrusion",
            "severity": "high",
            "description": "Port scan detected",
            "ip_address": "8.8.8.8"
        }
        
        response = self.client.post(url, data, HTTP_USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)
        
        self.assertEqual(response.data['source_name'], 'Firewall-01')
        
    def test_invalid_severity(self):
        url = reverse('events-ingest')
        data = {
            "source_name": "Firewall-01",
            "event_type": "intrusion",
            "severity": "invalid_level",
            "description": "Test"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['status'], 'error')
        self.assertIn('severity', response.data['data'])
