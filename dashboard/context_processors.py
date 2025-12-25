from alerts.models import Alert

def notification_context(request):
    unresolved_count = 0
    if request.user.is_authenticated:
        unresolved_count = Alert.objects.filter(status='open').count()
    return {
        'unresolved_count': unresolved_count
    }
