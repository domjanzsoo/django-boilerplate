from django.test import TestCase
from django.contrib.auth import get_user_model


class UserManagerTestCase(TestCase):
    def setUp(self):
        self.data = {
            "user": {
                "email": "normal@user.com",
                "password": "foo",
                "first_name": "Joe",
                "last_name": "Doe"
            }
        }
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(**self.data['user'])
        self.assertEquals(user.email, self.data['user']['email'])
        self.assertEquals(user.first_name, self.data['user']['first_name'])
        self.assertEquals(user.last_name, self.data['user']['last_name'])
        self.assertTrue(user.is_active)
