from django.core.management.base import BaseCommand

from app.domain.models.user import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(email="admin@admin.com").exists():
            user = User.objects.create(
                email="admin@admin.com.br",
                username="admin",
                full_name="Admin",
                is_superuser=True,
                is_staff=True,
                cpf="123123",
                phone="123123",
                birthdate='1998-01-01'
            )
            user.set_password("123")
            user.save()
