import uuid
from django.db import models
from django.utils import timezone

from app.domain.models.user import User
from app.domain.models.transfer import Transfer


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    transfer = models.ForeignKey(Transfer, on_delete=models.SET_NULL, null=True)
    text = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
