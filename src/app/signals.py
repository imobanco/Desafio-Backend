from django.db.models.signals import post_save
from django.dispatch import receiver

from app.domain.models.user import User
from app.domain.repositories.account import AccountRepository


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        AccountRepository().create_account(instance)
