from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from django.test import TestCase

from app.domain.models.user import User
from app.domain.repositories.user import UserRepository
from app.services.users import UserService


class UserServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.service = UserService(UserRepository())
        cls.user = User.objects.get_or_create(
            email="user@email.com",
            full_name="user",
            cpf="123123",
            phone="123123",
            birthdate="1998-01-01",
        )[0]

    def test_get_user_by_id(self):
        response = self.service.get_user(id=self.user.id)
        self.assertEqual(response.email, self.user.email)
        self.assertEqual(response.full_name, self.user.full_name)

    def test_get_user_by_request(self):
        request = Request
        request.user = self.user

        response = self.service.get_user(request=request)
        self.assertEqual(response.email, self.user.email)
        self.assertEqual(response.full_name, self.user.full_name)

    def test_post_user(self):
        request = Request
        data = {
            "password": "123",
            "username": "mahomes",
            "email": "mahomes@chiefs.com",
            "full_name": "Mahomes",
            "birthdate": "1998-01-23",
            "phone": "00-00-00",
            "cpf": "00-00-00",
        }
        request.data = data

        response = self.service.post_user(request=request)

        self.assertEqual(response.username, data["username"])
        self.assertTrue(User.objects.filter(username="mahomes").exists())

    def test_put_user(self):
        request = Request
        data = {
            "password": "123",
            "username": "mahomes",
            "email": "mahomes@chiefs.com",
            "full_name": "Mahomes",
            "birthdate": "1998-01-23",
            "phone": "00-00-00",
            "cpf": "00-00-00",
        }
        request.data = data
        request.user = self.user

        response = self.service.put_user(request=request)

        self.assertEqual(response.full_name, data["full_name"])
        self.assertTrue(User.objects.filter(email="user@email.com").exists())
        self.assertEqual(User.objects.filter(email="user@email.com").count(), 1)
