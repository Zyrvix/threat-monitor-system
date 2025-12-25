import logging
import json
from rest_framework import viewsets, permissions, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from .utils import get_client_ip, enrich_event_data, get_device_info

logger = logging.getLogger('security')

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['event_type', 'severity', 'source_name']
    search_fields = ['description', 'source_name']
    ordering_fields = ['timestamp']

    def perform_create(self, serializer):
        request = self.request
        
        ip = serializer.validated_data.get('ip_address') or get_client_ip(request) 
        geo_data = enrich_event_data(ip) or {}
        device_data = get_device_info(request.user_agent)
        headers = {k: v for k, v in request.META.items() if k.startswith('HTTP_')}
        instance = serializer.save(
            ip_address=ip,
            request_method=request.method,
            request_path=request.path,
            headers_dump=headers,
            **geo_data,
            **device_data
        )
        
        logger.info(f"THREAT_INGEST: [{instance.severity.upper()}] {instance.event_type} "
                    f"from {instance.source_name} | Location: {instance.city}, {instance.country} "
                    f"| Device: {instance.device_type} ({instance.os_family})")

    @action(detail=False, methods=['post'], url_path='ingest')
    def ingest(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
