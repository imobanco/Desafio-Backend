from django.urls import path

from api.services.users import UserDetailsService, UserMeService, UserCreateService


urlpatterns = [
    path('users/', UserCreateService.as_view()),
    path('users/<uuid:id>/', UserDetailsService.as_view()),
    path('users/me/', UserMeService.as_view()),
]