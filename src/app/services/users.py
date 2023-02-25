
from uuid import UUID

from rest_framework.request import Request

from app.domain.repositories.user import UserRepository
from app.domain.models.user import User


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.model = User

    def get_user(self, id: UUID = None, request: Request = None) -> User:
        if id:
            user = self.user_repository.find_user(id=id)
        else:
            user = self.user_repository.find_user(user=request.user)
        return user

    def post_user(self, request: Request) -> User:
        data = request.data
        password = data.get('password')

        user = self.user_repository.create_user(data, password)
        return user

    def put_user(self, request: Request) -> User:
        data = request.data
        data.pop('email')
        data.pop('username')
        password = data.pop('password')

        user = self.user_repository.update_user(request.user, data, password)
        return user
