from typing import Dict, List
from django.db.models import Q
from app.domain.models.account import Account

from app.domain.repositories.base import BaseRepository

from app.domain.models.deposit import Deposit
from app.domain.models.user import User


class DepositRepository(BaseRepository):
    def __init__(self) -> None:
        self.model = Deposit

    def _increase_balance(self, account: Account, value: float):
        account.balance += value
        account.save()

    def create_deposit(self, data: Dict, user: User) -> Deposit:
        account = user.account_set.first()
        data["account_id"] = account.id
        deposit = self.create(data)
        self._increase_balance(account, deposit.value)
        return deposit

    def find_deposits(self, user: User) -> List[Deposit]:
        account = user.account_set.first()
        query = Q(account=account)
        deposits = self.find_by_query(query)
        return deposits
