from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

from resources.repositories.account_repository import AccountRepository
from resources.serializers.account_serialize import AccountSerializer


class AccountMeService(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        account = AccountRepository().get_account(request.user)
        serializer = AccountSerializer(account, many=False)
        return Response(serializer.data)