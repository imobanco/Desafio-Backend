from app.domain.repositories.base import BaseRepository
from app.domain.models.user import User
from app.domain.models.account import Account


class AccountRepository(BaseRepository):

    def create_account(self, user: User) -> Account:
        data = {'balance': 0.0}
        account = self.create(data)
        account.user = user
        account.save()
        return account

    def find_account(self, user: User) -> Account:
        account = self.find(id=user.account_set.first().id)
        return account
