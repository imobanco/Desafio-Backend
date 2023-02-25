import uuid
from django.db import models
from app.domain.models import User


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    balance = models.FloatField(null=True)
