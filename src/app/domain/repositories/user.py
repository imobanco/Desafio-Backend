from app.domain.repositories.base import BaseRepository
from app.domain.models.user import User


class UserRepository(BaseRepository):

    def create_user(self, request, password) -> User:
        user = self.create(request)
        user.set_password(password)
        user.save()

        return user

    def update_user(self, request, id) -> User:
        password = request.pop('password')
        request.pop('email')
        request.pop('username')
        user = self.update(id, request)
        if password:
            user.set_password(password)
            user.save()
        return user
