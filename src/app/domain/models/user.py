import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=240)
    birthdate = models.DateField()
    phone = models.CharField(max_length=50)
    cpf = models.CharField(max_length=30)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
