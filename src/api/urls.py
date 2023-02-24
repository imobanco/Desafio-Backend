from django.urls import path

from api.services.users import UserDetailsService, UserMeService, UserCreateService
from api.services.account import AccountMeService
from api.services.deposit import DepositCreateService
from api.services.transfer import TransferCreateService


urlpatterns = [
    path('users/', UserCreateService.as_view()),
    path('users/<uuid:id>/', UserDetailsService.as_view()),
    path('users/me/', UserMeService.as_view()),

    path('accounts/me/', AccountMeService.as_view()),

    path('deposit/', DepositCreateService.as_view()),

    path('transfer/', TransferCreateService.as_view()),
]