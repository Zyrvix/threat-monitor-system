from rest_framework import generics, permissions
from .serializers import UserSerializer
from .models import CustomUser

from .utils import log_user_activity

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        log_user_activity(
            user, 
            'user_registered', 
            'accounts', 
            f"API: New user {user.username} registered.",
            self.request
        )
