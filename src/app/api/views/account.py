from django.db.models import Q
from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

from app.services.account import AccountService
from app.domain.repositories.account  import AccountRepository
from app.api.serializers.account import AccountSerializer


class AccountMeView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        account_service = AccountService(AccountRepository())
        query = Q(user=request.user)
        account = account_service.get_account(query=query)
        serializer = AccountSerializer(account, many=False)
        return Response(serializer.data)