from rest_framework.test import APIRequestFactory
from django.test import TestCase

from app.domain.models.account import Account
from app.domain.models.user import User

from app.domain.repositories.account import AccountRepository


class AccountRepositoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.repository = AccountRepository()
        cls.user = User.objects.get_or_create(
            email='user@email.com',
            full_name='user',
            cpf="123123",
            phone="123123",
            birthdate='1998-01-01'
        )[0]

    def test_repository_create_account(self):
        response = self.repository.create_account(self.user)

        self.assertTrue(isinstance(response, Account))
        self.assertTrue(Account.objects.filter(user=self.user).exists())

    def test_repository_find_account(self):
        response = self.repository.find_account(self.user)

        self.assertTrue(isinstance(response, Account))
