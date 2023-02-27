from rest_framework.test import APIRequestFactory
from django.test import TestCase
from app.domain.models.account import Account
from app.domain.models.transfer import Transfer

from app.domain.models.user import User
from app.domain.repositories.transfer import TransferRepository


class TransferRepositoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.repository = TransferRepository()
        cls.user = User.objects.get_or_create(
            email='user@email.com',
            full_name='user',
            cpf="123123",
            phone="123123",
            birthdate='1998-01-01'
        )[0]
        cls.account = Account.objects.get(user=cls.user)
        cls.account.balance = 200_000
        cls.account.save()

        cls.user1 = User.objects.get_or_create(
            username='user1',
            email='user1@email.com',
            full_name='user1',
            cpf="000111",
            phone="000111",
            birthdate='1998-01-01'
        )[0]

        cls.account1 = Account.objects.get(user=cls.user1)

    def test_repository_create_post_transfer(self):
        data = {
            "value": 10000,
            "destiny": self.account1.id,
            "description": "test 123",
            "public": True
            }

        response = self.repository.create_transfer(data, self.user)
        self.assertTrue(isinstance(response, Transfer))

    def test_repository_find_transfers(self):
        Transfer.objects.create(origin=self.account, destiny=self.account1, value=300)
        Transfer.objects.create(origin=self.account, destiny=self.account1, value=1000)

        response = self.repository.find_transfers(user=self.user)

        self.assertEqual(len(response), 2)

    def test_repository_find_public_transfers(self):
        Transfer.objects.create(
            origin=self.account,
            destiny=self.account1,
            value=1000,
            public=True)
        Transfer.objects.create(
            origin=self.account,
            destiny=self.account1,
            value=22,
            public=True)

        response = self.repository.find_public_transfers()

        self.assertEqual(len(response), 2)

    def test_repository_put_user(self):
        transfer = Transfer.objects.create(
            origin=self.account,
            description='Test',
            destiny=self.account1,
            value=12,
            public=True)

        data = {
            "description": "test 123"
        }

        response = self.repository.update_transfer(transfer.id, data)

        self.assertEqual(response.description, data['description'])
        self.assertTrue(Transfer.objects.filter(description=data['description']).exists())
