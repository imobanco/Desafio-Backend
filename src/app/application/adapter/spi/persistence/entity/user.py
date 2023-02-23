from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    full_name = models.CharField(max_length=240)
    email = models.CharField(max_length=240, unique=True)
    birthdate = models.DateField()
    phone = models.CharField(max_length=50)
    cpf = models.CharField(max_length=30)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
