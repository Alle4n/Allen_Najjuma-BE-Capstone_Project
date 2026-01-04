from rest_framework.test import APITestCase

class HelloWorldTest(APITestCase):
    def test_hello_world(self):
        self.assertEqual("Hello, World!", "Hello, World!")