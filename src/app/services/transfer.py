from uuid import UUID

from typing import  List
from django.db.models import Q
# from rest_framework.request import Request
from app.domain.models.transfer import Transfer
from app.domain.models.user import User
from app.domain.repositories.transfer import TransferRepository


class TransferService:
    def __init__(self, transfer_repository: TransferRepository):
        self.transfer_repository = transfer_repository
        self.model = Transfer

    def post_transfer(self, data, user) -> Transfer:
        if self._verify_account_price(user, data.get('value')):
            data = self._update_transfer_payload(user, data)
            transfer = self.transfer_repository.create(data)
            self._update_price_origin(user, data.get('value'))
            self._update_price_destiny(transfer.destiny, transfer.value )
            return transfer

    def get_transfers(self, user: User) -> List[Transfer]:
        account = user.account_set.first()
        query = Q(Q(origin=account) | Q(destiny=account))
        transfers = self.transfer_repository.find_by_query(query)
        return transfers

    def get_public_transfers(self) -> List[Transfer]:
        query = Q(public=True)
        transfers = self.transfer_repository.find_by_query(query)
        return transfers

    def put_transfer(self, id: UUID, data) -> Transfer:
        query = Q(public=True)
        transfer = self.transfer_repository.update(id, data,query)
        return transfer
