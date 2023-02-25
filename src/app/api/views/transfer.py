from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.domain.repositories.transfer import TransferRepository
from app.services.transfer import TransferService
from app.api.serializers.transfer import TransferMeSerializer, TransferSerializer


class TransferCreateView(views.APIView):
    permission_classes = (IsAuthenticated,)
    service = TransferService(TransferRepository())

    def post(self, request):
        transfer = self.service.post_transfer(request)
        serializer =TransferSerializer(transfer, many=False)
        return Response(serializer.data)

    def get(self, request):
        transfers = self.service.get_transfers(request)
        serializer = TransferMeSerializer(transfers, many=True)
        return Response(serializer.data)


class TransferPublicView(views.APIView):
    permission_classes = (IsAuthenticated,)
    service = TransferService(TransferRepository())

    def get(self, request):
        transfers = self.service.get_public_transfers()
        serializer = TransferMeSerializer(transfers, many=True)
        return Response(serializer.data)


class TransferDetailsView(views.APIView):
    permission_classes = (IsAuthenticated,)
    service = TransferService(TransferRepository())

    def patch(self, request, id):
        transfer = self.service.put_transfer(id, request)
        serializer = TransferMeSerializer(transfer)
        return Response(serializer.data)
