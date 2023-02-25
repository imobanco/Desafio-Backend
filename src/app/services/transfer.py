from uuid import UUID

from typing import  List
from rest_framework.request import Request

from app.domain.models.transfer import Transfer
from app.domain.repositories.transfer import TransferRepository


class TransferService:
    def __init__(self, transfer_repository: TransferRepository):
        self.transfer_repository = transfer_repository
        self.model = Transfer

    def post_transfer(self, request: Request) -> Transfer:
        transfer = self.transfer_repository.create_transfer(request.data, request.user)
        return transfer


    def get_transfers(self, request: Request) -> List[Transfer]:
        transfers = self.transfer_repository.find_transfers(request.user)
        return transfers

    def get_public_transfers(self) -> List[Transfer]:
        transfers = self.transfer_repository.find_public_transfers()
        return transfers

    def put_transfer(self, id: UUID, request: Request) -> Transfer:
        transfer = self.transfer_repository.update_transfer(id, request.data)
        return transfer
