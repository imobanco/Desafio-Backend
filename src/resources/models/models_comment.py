import uuid
from django.db import models
from django.utils import timezone

from resources.models.models_transfer import Transfer 
from resources.models.models_user import User


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    transfer = models.ForeignKey(Transfer, on_delete=models.SET_NULL, null=True)
    text = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
