from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from django.test import TestCase

from app.domain.models.account import Account
from app.domain.models.deposit import Deposit
from app.domain.models.user import User

from app.domain.repositories.deposity import DepositRepository
from app.services.deposit import DepositService


class DepositServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.service = DepositService(DepositRepository())

        cls.user = User.objects.get_or_create(
            email="user@email.com",
            full_name="user",
            cpf="123123",
            phone="123123",
            birthdate="1998-01-01",
        )[0]
        cls.account = Account.objects.get(user=cls.user)
        Deposit.objects.create(account=cls.account, value=200)

    def test_create_deposit(self):
        data = {"value": 10000, "description": "add funds"}
        request = Request
        request.user = self.user
        request.data = data

        response = self.service.create_deposit(request)
        self.assertEqual(Deposit.objects.filter(account=self.account).count(), 2)
        self.assertEqual(response.value, 10000)

    def test_get_deposit(self):
        request = Request
        request.user = self.user

        response = self.service.get_deposits(request)

        self.assertEqual(len(response), 1)
