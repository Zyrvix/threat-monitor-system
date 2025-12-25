from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'severity', 'source_name', 'ip_address', 'country', 'timestamp')
    list_filter = ('severity', 'event_type', 'country')
    search_fields = ('source_name', 'ip_address', 'description')
    readonly_fields = (
        'ip_address', 'city', 'state', 'country', 'latitude', 'longitude',
        'isp', 'asn', 'is_proxy', 'is_vpn', 'device_type', 'os_family',
        'os_version', 'browser_family', 'browser_version', 'user_agent_string',
        'request_method', 'request_path', 'headers_dump', 'timestamp'
    )
