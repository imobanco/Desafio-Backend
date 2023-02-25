from typing import List
from rest_framework.request import Request

from app.domain.models.deposit import Deposit
from app.domain.repositories.deposity import DepositRepository


class DepositService:
    def __init__(self, comment_repository: DepositRepository):
        self.comment_repository = comment_repository
        self.model = Deposit

    def create_deposit(self, request: Request) -> Deposit:
        deposit = self.comment_repository.create_deposit(request.data, request.user)
        return deposit

    def get_deposits(self, request: Request) -> List[Deposit]:
        deposits = self.comment_repository.find_deposits(request.user)
        return deposits
