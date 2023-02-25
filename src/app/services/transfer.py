from uuid import UUID

from typing import Dict, List
from django.db.models import Q
from app.domain.models.transfer import Transfer
from app.domain.models.user import User
from app.domain.repositories.transfer import TransferRepository


class TransferService:
    def __init__(self, transfer_repository: TransferRepository):
        self.transfer_repository = transfer_repository
        self.model = Transfer
    
    def _verify_account_price(self, user, value):
        if user.account_set.first().balance >= value:
            return True
        return False
    
    def _update_transfer_payload(self, user, payload) -> Dict:
        destiny_id = payload.pop('destiny')
        payload['origin_id'] = user.account_set.first().id
        payload['destiny_id'] = destiny_id
        return payload

    def _update_price_origin(self, user, value):
        account = user.account_set.first()
        account.balance -= value
        account.save()

    def _update_price_destiny(self, account, value):
        account.balance += value
        account.save()

    def create_transfer(self, data, user) -> Transfer:        
        if self._verify_account_price(user, data.get('value')):
            data = self._update_transfer_payload(user, data)
            transfer = self.transfer_repository.create(data)
            self._update_price_origin(user, data.get('value'))
            self._update_price_destiny(transfer.destiny, transfer.value )
            return transfer
    
    def me_transfers(self, user: User) -> List[Transfer]:
        account = user.account_set.first()
        query = Q(Q(origin=account) | Q(destiny=account))
        transfers = self.transfer_repository.find_all(query)
        return transfers

    def get_public_transfers(self) -> List[Transfer]:
        query = Q(public=True)
        transfers = self.transfer_repository.find_all(query)
        return transfers

    def update_transfer(self, id: UUID, data) -> Transfer:
        query = Q(public=True)
        transfer = self.transfer_repository.update(id, data,query)
        return transfer