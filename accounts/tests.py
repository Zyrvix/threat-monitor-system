from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

User = get_user_model()

class UserAccountTests(APITestCase):
    def test_user_registration(self):
        url = reverse('api-register')
        data = {
            "username": "test_analyst",
            "email": "analyst@example.com",
            "password": "securepassword123",
            "role": "analyst"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        
        user = User.objects.get(username="test_analyst")
        self.assertEqual(user.role, "analyst")

    def test_superuser_auto_admin_role(self):
        superuser = User.objects.create_superuser(
            username="bigboss", 
            email="boss@example.com", 
            password="adminpassword"
        )
        self.assertEqual(superuser.role, "admin")

    def test_login_and_jwt(self):
        User.objects.create_user(username="user1", password="password123")
        url = reverse('token_obtain_pair')
        data = {"username": "user1", "password": "password123"}
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
