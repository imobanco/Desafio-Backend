from typing import Dict
from uuid import UUID
from app.domain.repositories.base import BaseRepository
from app.domain.models.user import User


class UserRepository(BaseRepository):

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
