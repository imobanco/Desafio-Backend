from typing import Dict, List
from django.db.models import Q

from app.domain.repositories.base import BaseRepository

from app.domain.models.deposit import Deposit
from app.domain.models.user import User


class DepositRepository(BaseRepository):
    def __init__(self) -> None:
        self.model = Deposit

    def _update_balance(self, account, value):
        account.balance += value
        account.save()
    
    def create_deposit(self, data: Dict, user: User) -> Deposit:
        account = user.account_set.first()
        data['account_id'] = account.id
        deposit = self.create(data)
        self._update_balance(account, deposit.value)
        deposit.save()
        return deposit
    
    def get_all_deposits(self, user) -> List[Deposit]:
        account = user.account_set.first()
        query = Q(account=account)
        deposits = self.find_all(query)
        return deposits
