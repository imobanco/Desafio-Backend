from rest_framework.test import APIRequestFactory
from django.test import TestCase

from app.domain.models.account import Account
from app.domain.models.deposit import Deposit
from app.domain.models.user import User

from app.domain.repositories.deposity import DepositRepository


class DepositRepositoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.repository = DepositRepository()

        cls.user = User.objects.get_or_create(
            email="user@email.com",
            full_name="user",
            cpf="123123",
            phone="123123",
            birthdate="1998-01-01",
        )[0]
        cls.account = Account.objects.get(user=cls.user)
        Deposit.objects.create(account=cls.account, value=200)

    def test_repository_create_deposit(self):
        data = {"value": 24_000, "description": "add funds"}

        response = self.repository.create_deposit(data, self.user)

        self.assertEqual(Deposit.objects.filter(description="add funds").count(), 1)
        self.assertEqual(response.value, 24_000)

    def test_repository_find_deposits(self):
        response = self.repository.find_deposits(user=self.user)

        self.assertEqual(len(response), 1)

    def test_repository_increase_balance(self):
        self.repository._increase_balance(self.account, 2000)

        self.assertEqual(Account.objects.get(user=self.user).balance, 2000)
