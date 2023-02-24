from typing import Dict
import uuid
from resources.repositories.base_repository import BaseRepository
from resources.models import Account, User, Transfer


class TransferRepository(BaseRepository):
    def __init__(self) -> None:
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
            transfer = self.create(data)
            self._update_price_origin(user, data.get('value'))
            self._update_price_destiny(transfer.destiny, transfer.value )
            return transfer
