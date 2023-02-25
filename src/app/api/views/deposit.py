from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.services.deposit import DepositService
from app.domain.repositories.deposity import DepositRepository
from app.api.serializers.deposit import DepositSerializer


class DepositCreateView(views.APIView):
    permission_classes = (IsAuthenticated,)
    service = DepositService(DepositRepository())
    serializer_class = DepositSerializer

    def post(self, request, format=None):
        deposit = self.service.create_deposit(request)
        serializer = DepositSerializer(deposit, many=False)
        return Response(serializer.data)

    def get(self, request, format=None):
        deposit = self.service.get_deposits(request)
        serializer = DepositSerializer(deposit, many=True)
        return Response(serializer.data)
