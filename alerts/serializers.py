from rest_framework import serializers
from .models import Alert
from events.serializers import EventSerializer

class AlertSerializer(serializers.ModelSerializer):
    event_details = EventSerializer(source='event', read_only=True)
    assigned_to_username = serializers.ReadOnlyField(source='assigned_to.username')

    class Meta:                                                                                                                                                                                                                                                                                                                                                                                                          
        model = Alert
        fields = ('id', 'event', 'event_details', 'status', 'assigned_to', 'assigned_to_username', 'created_at', 'updated_at', 'resolution_notes')
        read_only_fields = ('created_at', 'updated_at')

    def validate_status(self, value):
        from constants import ALERT_STATUS
        valid_statuses = [choice[0] for choice in ALERT_STATUS]
        if value.lower() not in valid_statuses:
            raise serializers.ValidationError(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
        return value.lower()
