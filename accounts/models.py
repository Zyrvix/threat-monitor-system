from django.contrib.auth.models import AbstractUser
from django.db import models

from constants import USER_ROLES

class CustomUser(AbstractUser):
    role = models.CharField(max_length=10, choices=USER_ROLES, default='analyst')

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = 'admin'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.role})"


class UserActivity(models.Model):
    from constants import ACTIVITY_ACTIONS, ACTIVITY_MODULES
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='activities')
    action = models.CharField(max_length=50, choices=ACTIVITY_ACTIONS)
    module = models.CharField(max_length=50, choices=ACTIVITY_MODULES)
    description = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = "User Activities"

    def __str__(self):
        return f"{self.user.username} - {self.action} ({self.timestamp})"
