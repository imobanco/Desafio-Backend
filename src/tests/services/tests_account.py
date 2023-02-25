from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from django.test import TestCase

from app.domain.models.account import Account
from app.domain.models.user import User

from app.domain.repositories.account import AccountRepository
from app.services.account import AccountService


class AccountServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.service = AccountService(AccountRepository())
        cls.user = User.objects.get_or_create(
            email='user@email.com',
            full_name='user',
            cpf="123123",
            phone="123123",
            birthdate='1998-01-01'
        )[0]

    def test_get_account_by_user(self):
        request = Request
        request.user = self.user
        response = self.service.get_account(request)
        self.assertTrue(Account.objects.filter(user=self.user).exists())
        self.assertEqual(
            response.balance,
            Account.objects.get(user=self.user).balance)
