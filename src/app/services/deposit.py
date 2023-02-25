from typing import Dict, List
from django.db.models import Q

from app.domain.models.deposit import Deposit
from app.domain.models.user import User
from app.domain.repositories.deposity import DepositRepository


class DepositService:
    def __init__(self, comment_repository: DepositRepository):
        self.comment_repository = comment_repository
        self.model = Deposit

    def _update_balance(self, account, value):
        account.balance += value
        account.save()
    
    def create_deposit(self, data: Dict, user: User) -> Deposit:
        account = user.account_set.first()
        data['account_id'] = account.id
        deposit = self.comment_repository.create(data)
        self._update_balance(account, deposit.value)
        deposit.save()
        return deposit
    
    def get_all_deposits(self, user) -> List[Deposit]:
        account = user.account_set.first()
        query = Q(account=account)
        deposits = self.comment_repository.find_all(query)
        return deposits
