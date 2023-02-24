from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

from resources.repositories.transfer_repository import TransferRepository
from resources.serializers.transfer_serialize import TransferSerializer


class TransferCreateService(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        transfer = TransferRepository().create_transfer(request.data, request.user)
        serializer =TransferSerializer(transfer, many=False)
        return Response(serializer.data)