from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

from resources.repositories.transfer_repository import TransferRepository
from resources.serializers.transfer_serialize import TransferMeSerializer, TransferSerializer


class TransferCreateView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        transfer = TransferRepository().create_transfer(request.data, request.user)
        serializer =TransferSerializer(transfer, many=False)
        return Response(serializer.data)
    
    def get(self, request):
        transfers = TransferRepository().me_transfers(request.user)
        serializer = TransferMeSerializer(transfers, many=True)
        return Response(serializer.data)


class TransferPublicView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        transfers = TransferRepository().get_public_transfers()
        serializer = TransferMeSerializer(transfers, many=True)
        return Response(serializer.data)


class TransferDetailsView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def patch(self, request, id):
        transfer = TransferRepository().update_transfer(id, request.data)
        serializer = TransferMeSerializer(transfer)
        return Response(serializer.data)
