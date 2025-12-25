from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Alert
from .serializers import AlertSerializer
from accounts.permissions import IsAdminOrReadOnly
from accounts.utils import log_user_activity

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all().select_related('event', 'assigned_to')
    serializer_class = AlertSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'event__severity']
    ordering_fields = ['created_at', 'updated_at']

    def perform_update(self, serializer):
        old_status = self.get_object().status
        instance = serializer.save()
        
        action = 'alert_resolved' if instance.status == 'resolved' else 'alert_acknowledged'
        log_user_activity(
            self.request.user,
            action,
            'alerts',
            f"API: Changed Alert #{instance.id} from {old_status} to {instance.status}.",
            self.request
        )

        import logging
        logger = logging.getLogger('security')
        logger.info(f"ALERT_UPDATE: Alert {instance.id} state changed to {instance.status} by {self.request.user.username}")
