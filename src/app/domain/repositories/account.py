from app.domain.repositories.base import BaseRepository
from app.domain.models.user import User
from app.domain.models.account import Account


class AccountRepository(BaseRepository):
    def __init__(self) -> None:
        self.model = Account
    
    def create_account(self, user: User) -> Account:
        data = {'balance': 0.0}
        account = self.create(data)
        account.user = user
        account.save()
        return account

    def get_account(self, user) -> Account:
        account = self.find(id=user.account_set.first().id)
        return account