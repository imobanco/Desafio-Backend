import uuid
from django.db import models
from django.utils import timezone

from resources.models.models_account import Account


class Deposit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    value = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)
