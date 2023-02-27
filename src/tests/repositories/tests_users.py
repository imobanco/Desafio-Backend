from rest_framework.test import APIRequestFactory
from django.test import TestCase

from app.domain.models.user import User
from app.domain.repositories.user import UserRepository


class UserServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.repository = UserRepository()
        cls.user = User.objects.get_or_create(
            email="user@email.com",
            full_name="user",
            cpf="123123",
            phone="123123",
            birthdate="1998-01-01",
        )[0]

    def test_repository_find_user_by_id(self):
        response = self.repository.find_user(id=self.user.id)
        self.assertEqual(response.email, self.user.email)
        self.assertEqual(response.full_name, self.user.full_name)

    def test_repository_find_user_by_request(self):
        response = self.repository.find_user(user=self.user)
        self.assertEqual(response.email, self.user.email)
        self.assertEqual(response.full_name, self.user.full_name)

    def test_repository_update_user(self):
        data = {
            "username": "mahomes",
            "email": "mahomes@chiefs.com",
            "full_name": "Mahomes",
            "birthdate": "1998-01-23",
            "phone": "00-00-00",
            "cpf": "00-00-00",
        }

        response = self.repository.update_user(self.user, data)

        self.assertEqual(response.username, data["username"])
        self.assertTrue(User.objects.filter(username="mahomes").exists())
