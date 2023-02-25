from typing import List
from rest_framework.request import Request
from app.domain.models.account import Account
from app.domain.repositories.account import AccountRepository


class AccountService:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository
        self.model = Account

    def get_account(self, request: Request) -> List[Account]:
        account = self.account_repository.find_account(request.user)
        return account
