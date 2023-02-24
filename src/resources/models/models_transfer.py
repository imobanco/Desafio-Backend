import uuid
from django.db import models
from django.utils import timezone
from resources.models.models_account import Account


class Transfer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    origin = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='transfer_origin', null=True)
    destiny = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='transfer_destiny', null=True)
    value = models.FloatField(null=True)
    description = models.TextField(null=True)
    public = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
