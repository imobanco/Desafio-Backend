from django.db.models.signals import post_save
from django.dispatch import receiver
from resources.models.models_user import User
from resources.repositories.account_repository import AccountRepository
 
 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        AccountRepository().create_account(instance)