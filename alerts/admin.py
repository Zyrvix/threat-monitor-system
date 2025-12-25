from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'status', 'assigned_to', 'created_at')
    list_filter = ('status', 'event__severity')
    search_fields = ('event__event_type', 'resolution_notes')
    ordering = ('-created_at',)
