from rest_framework import views

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.services.account import AccountService
from app.domain.repositories.account  import AccountRepository
from app.api.serializers.account import AccountSerializer


class AccountMeView(views.APIView):
    permission_classes = (IsAuthenticated,)
    service = AccountService(AccountRepository())
    serializer_class = AccountSerializer

    def get(self, request):
        account = self.service.get_account(request)
        serializer = self.serializer_class(account, many=False)
        return Response(serializer.data)
