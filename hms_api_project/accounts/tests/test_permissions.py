from rest_framework.test import APITestCase
from accounts.models import User

class UserPermissionTest(APITestCase):

    def test_unauthenticated_access_denied(self):
        response = self.client.get("/api/patients/")
        self.assertEqual(response.status_code, 401)
