from resources.repositories.base_repository import BaseRepository
from resources.models.models_user import User


class UserRepository(BaseRepository):
    def __init__(self) -> None:
        self.model = User
    
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
