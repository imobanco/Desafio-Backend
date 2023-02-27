import uuid
from typing import Dict, List

from django.db.models import Q

from app.domain.repositories.base import BaseRepository
from app.domain.models.user import User
from app.domain.models.account import Account
from app.domain.models.transfer import Transfer


class TransferRepository(BaseRepository):
    def __init__(self) -> None:
        self.model = Transfer

    def verify_account_balance(self, account: Account, value: float) -> bool:
        return account.balance >= value

    def decrease_balance(self, account, value):
        account.balance -= value
        account.save()

    def increase_balance(self, account, value):
        account.balance += value
        account.save()

    def create_transfer(self, data: Dict, user: User) -> Transfer:
        account = user.account_set.first()
        data["origin_id"] = account.id
        data["destiny_id"] = data.pop("destiny")
        if self.verify_account_balance(account, data.get("value")):
            transfer = self.create(data)
            self.decrease_balance(transfer.origin, transfer.value)
            self.increase_balance(transfer.destiny, transfer.value)
            return transfer

    def find_transfers(self, user: User) -> List[Transfer]:
        account = user.account_set.first()
        query = Q(Q(origin=account) | Q(destiny=account))
        transfers = self.find_by_query(query)
        return transfers

    def find_public_transfers(self) -> List[Transfer]:
        transfers = self.find_by_query(Q(public=True))
        return transfers

    def update_transfer(self, id: uuid.UUID, data: Dict) -> Transfer:
        transfer = self.update(id, data, Q(public=True))
        return transfer

    def delete_transfer(self, id: uuid.UUID) -> None:
        transfer = self.find(id)

        value = transfer.value
        self.remove(id)
        self.decrease_balance(transfer.destiny, value)
        self.increase_balance(transfer.origin, value)
