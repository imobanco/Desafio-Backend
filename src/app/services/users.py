
from app.domain.models.user import User

from app.domain.repositories.base import BaseRepository
from app.domain.repositories.user import UserRepository
from app.domain.models.user import User


class UserRepository(BaseRepository):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.model = User

    def create_user(self, request, password) -> User:
        user = self.user_repository.create(request)
        user.set_password(password)
        user.save()
        return user

    def update_user(self, request, id) -> User:
        password = request.pop('password')
        request.pop('email')
        request.pop('username')
        user = self.user_repository.update(id, request)
        if password:
            user.set_password(password)
            user.save()
        return user
