from typing import Dict
from uuid import UUID
from xmlrpc.client import boolean
from django.db.models import Q
from app.domain.repositories.base import BaseRepository
from app.domain.models.user import User


class UserRepository(BaseRepository):
    def __init__(self) -> None:
        self.model = User

    def find_user_exist(self, email: str) -> boolean:
        user =  self.find_by_query(query=Q(email=email))
        return user.exists()

    def find_user(self, id: UUID = None, user: User = None):
        if id:
            user = self.find(id)
        else:
            user = self.find(user.id)

        return user

    def create_user(self, data: Dict, password: str) -> User:
        user = self.create(data)
        user.set_password(password)
        user.save()
        return user

    def update_user(self, user: User, data: Dict, password: str = None) -> User:
        user = self.update(user.id, data)
        if password:
            user.set_password(password)
            user.save()
        return user
