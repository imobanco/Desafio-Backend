from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from django.test import TestCase

from app.domain.models.account import Account
from app.domain.models.comment import Comment
from app.domain.models.transfer import Transfer
from app.domain.models.user import User

from app.domain.repositories.comment import CommentRepository
from app.services.comment import CommentService


class CommentServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.service = CommentService(CommentRepository())
        cls.user = User.objects.get_or_create(
            email="user@email.com",
            full_name="user",
            cpf="123123",
            phone="123123",
            birthdate="1998-01-01",
        )[0]
        cls.account = Account.objects.get(user=cls.user)

        cls.user1 = User.objects.get_or_create(
            username="user1",
            email="user1@email.com",
            full_name="user1",
            cpf="000111",
            phone="000111",
            birthdate="1998-01-01",
        )[0]

        cls.account1 = Account.objects.get(user=cls.user1)

        cls.tranfer = Transfer.objects.get_or_create(
            origin=cls.account, destiny=cls.account1, value=100, public=True
        )[0]

    def test_post_comment(self):
        request = Request
        request.user = self.user
        data = {"text": "that is crazy", "transfer_id": self.tranfer.id}
        request.data = data

        response = self.service.post_comment(request)
        self.assertEqual(Comment.objects.all().count(), 1)
        self.assertEqual(Comment.objects.get(text="that is crazy").id, response.id)

    def test_get_comments(self):
        Comment.objects.create(user=self.user, transfer=self.tranfer)
        Comment.objects.create(user=self.user, transfer=self.tranfer)
        Comment.objects.create(user=self.user, transfer=self.tranfer)
        Comment.objects.create(user=self.user, transfer=self.tranfer)
        request = Request
        request.user = self.user
        response = self.service.get_comments(request)

        self.assertEqual(len(response), 4)

    def test_get_comment(self):
        comment = Comment.objects.create(user=self.user, transfer=self.tranfer)
        request = Request
        request.user = self.user
        response = self.service.get_comment(comment.id)

        self.assertTrue(response)

    def test_put_comment(self):
        data = {"text": "go go eagles"}
        comment = Comment.objects.create(user=self.user, transfer=self.tranfer)
        request = Request
        request.user = self.user
        request.data = data
        response = self.service.put_comment(comment.id, request)

        self.assertEqual(response.text, data["text"])
