from django.urls import path

from api.services.users import UserDetailsService, UserMeService, UserCreateService
from api.services.account import AccountMeService
from api.services.deposit import DepositCreateService
from api.services.transfer import TransferCreateService, TransferPublicService, TransferDetailsService
from api.services.comment import CommentCreateService


urlpatterns = [
    path('users/', UserCreateService.as_view()),
    path('users/<uuid:id>/', UserDetailsService.as_view()),
    path('users/me/', UserMeService.as_view()),

    path('accounts/me/', AccountMeService.as_view()),

    path('deposit/', DepositCreateService.as_view()),

    path('transfer/', TransferCreateService.as_view()),
    path('transfer/public/', TransferPublicService.as_view()),
    path('transfer/<uuid:id>/', TransferDetailsService.as_view()),

    path('comment/', CommentCreateService.as_view()),
]