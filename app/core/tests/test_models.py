from django.contrib.auth import get_user_model
from django.test import TestCase

class CreateModel(TestCase):

    def test_Username(self):
        
        email='test@gmail.com'
        password='Testpass123'

        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_lower_email(self):
        email="test@Gmail.com"
        user=get_user_model().objects.create_user(email,"mahdi123")
        
        self.assertEqual(user.email,email.lower())

    def test_email_not_none(self):

        with self.assertRaises(ValueError):
            user=get_user_model().objects.create_user(None,"mahdi123")

    def test_is_superuser(self):
        
        superuser=get_user_model().objects.create_superuser("mahdi@gmail.com","mahdi123")
        