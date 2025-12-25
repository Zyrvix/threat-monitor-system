from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = (
            'created_at', 'updated_at', 'city', 'state', 'country', 'latitude', 'longitude', 
            'isp', 'asn', 'is_proxy', 'is_vpn', 'device_type', 
            'os_family', 'os_version', 'browser_family', 'browser_version', 
            'user_agent_string', 'request_method', 
            'request_path', 'headers_dump'
        )

    def validate_severity(self, value):
        from constants import SEVERITY_LEVELS
        valid_severities = [choice[0] for choice in SEVERITY_LEVELS]
        if value.lower() not in valid_severities:
            raise serializers.ValidationError(f"Invalid severity level. Must be one of: {', '.join(valid_severities)}")
        return value.lower()

    def validate_source_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Source name must be at least 3 characters long.")
        return value
