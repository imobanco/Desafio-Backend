from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from django.test import TestCase
from app.domain.models.account import Account
from app.domain.models.transfer import Transfer

from app.domain.models.user import User
from app.domain.repositories.transfer import TransferRepository
from app.services.transfer import TransferService


class TransferServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.service = TransferService(TransferRepository())
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

    def test_post_transfer(self):
        request = Request
        data = {
            "value": 10000,
            "destiny": self.account1.id,
            "description": "test 123",
            "public": True
            }
        request.data = data
        request.user = self.user

        response = self.service.post_transfer(request=request)
        # import pdb ; pdb.set_trace()
        self.assertTrue(isinstance(response, Transfer))

    def test_get_transfers(self):
        request = Request
        request.user = self.user
        Transfer.objects.create(origin=self.account, destiny=self.account1, value=12)
        Transfer.objects.create(origin=self.account, destiny=self.account1, value=100)
        Transfer.objects.create(origin=self.account, destiny=self.account1, value=20)
        Transfer.objects.create(origin=self.account, destiny=self.account1, value=300)
        Transfer.objects.create(origin=self.account, destiny=self.account1, value=1000)

        response = self.service.get_transfers(request=request)

        self.assertEqual(len(response), 5)

    def test_get_public_transfers(self):
        Transfer.objects.create(origin=self.account, destiny=self.account1,
            value=12, public=True)
        Transfer.objects.create(origin=self.account, destiny=self.account1, value=100)
        Transfer.objects.create(origin=self.account, destiny=self.account1,
            value=20, public=True)
        Transfer.objects.create(origin=self.account, destiny=self.account1, value=300)
        Transfer.objects.create(origin=self.account, destiny=self.account1,
            value=1000, public=True)

        response = self.service.get_public_transfers()

        self.assertEqual(len(response), 3)

    def test_put_user(self):
        transfer = Transfer.objects.create(
            origin=self.account,
            description='Test',
            destiny=self.account1,
            value=12,
            public=True)

        request = Request
        data = {
		"description": "test 123"
        }
        request.data = data
        request.user = self.user

        response = self.service.put_transfer(id=transfer.id, request=request)

        self.assertEqual(response.description, data['description'])
        self.assertTrue(Transfer.objects.filter(description=data['description']).exists())
