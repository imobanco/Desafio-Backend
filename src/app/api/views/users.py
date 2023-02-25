from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.services.users import UserService
from app.domain.repositories.user import UserRepository
from app.api.serializers.user import UserSerializer


class UserDetailsView(views.APIView):
    permission_classes = (IsAuthenticated,)
    service = UserService(UserRepository())

    def get(self, request, id, format=None):
        user = self.service.get_user(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserMeView(views.APIView):
    permission_classes = (IsAuthenticated,)
    service = UserService(UserRepository())

    def get(self, request):
        user = self.service.get_user(request=request)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request):
        user = self.service.put_user(request=request)

        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)


class UserCreateView(views.APIView):

    def post(self, request):
        password = request.data.get('password')
        user = UserRepository().create_user(request.data, password)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
