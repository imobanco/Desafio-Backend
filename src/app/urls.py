from django.urls import path

from app.api.views.users import UserDetailsView, UserMeView, UserCreateView
from app.api.views.account import AccountMeView
from app.api.views.deposit import DepositCreateView
from app.api.views.transfer import (
    TransferCreateView,
    TransferPublicView,
    TransferDetailsView,
)
from app.api.views.comment import CommentCreateView, CommentDetailsView


urlpatterns = [
    path("users/", UserCreateView.as_view()),
    path("users/<uuid:id>/", UserDetailsView.as_view()),
    path("users/me/", UserMeView.as_view()),
    path("accounts/me/", AccountMeView.as_view()),
    path("deposit/", DepositCreateView.as_view()),
    path("transfer/", TransferCreateView.as_view()),
    path("transfer/public/", TransferPublicView.as_view()),
    path("transfer/<uuid:id>/", TransferDetailsView.as_view()),
    path("comment/", CommentCreateView.as_view()),
    path("comment/<uuid:id>/", CommentDetailsView.as_view()),
]
