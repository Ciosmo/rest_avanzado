from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        """Probar creadno un nuevo usuario con un email correctamente"""
        email = 'testprogramchimp@ignacio.com' 
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Testea email para nuevo usuario normalizado """
        email = 'test@PROGRAMCHIMP.COM'
        user = get_user_model().objects.create_user(
            email,
            'test123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Nuevo usuario email invalido"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
            None,
            'test123'
        )

    def test_create_new_superuser(self):
        """Probar superuser creado"""
        email='test@programchimp.com'
        password='test123'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password 
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)