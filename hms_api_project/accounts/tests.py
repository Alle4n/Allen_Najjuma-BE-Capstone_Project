from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountsTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password123",
            role="admin"
        )

    def test_create_user(self):
        """Ensure a user is created correctly."""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.check_password("password123"))
        self.assertEqual(self.user.role, "admin")

    def test_obtain_token(self):
        """Ensure JWT token is returned for valid login."""
        url = reverse("token_obtain_pair")
        response = self.client.post(url, {
            "username": "testuser",
            "password": "password123"
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_users_list_requires_authentication(self):
        """Ensure /api/users/ requires authentication."""
        url = "/api/users/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Authenticate
        self.client.force_authenticate(user=self.user)
        authed_response = self.client.get(url)

        # Authenticated users should access it
        self.assertEqual(authed_response.status_code, status.HTTP_200_OK)
