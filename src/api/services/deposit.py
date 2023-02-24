from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

from resources.repositories.deposity_repository import DepositRepository
from resources.serializers.deposit_serialize import DepositSerializer


class DepositCreateService(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        deposit = DepositRepository().create_deposit(request.data, request.user)
        serializer = DepositSerializer(deposit, many=False)
        return Response(serializer.data)
    
    def get(self, request, format=None):
        deposit = DepositRepository().get_all_deposits(request.user)
        serializer = DepositSerializer(deposit, many=True)
        return Response(serializer.data)
