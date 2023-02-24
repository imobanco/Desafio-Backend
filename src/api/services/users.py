from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

from resources.repositories.user_repository import UserRepository
from resources.serializers.user_serialize import UserSerializer


class UserDetailsService(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        user = UserRepository().find(id=id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)



class UserMeService(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = UserRepository().find(id=request.user.id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def patch(self, request):
        user = UserRepository().update_user(request=request.data, id=request.user.id)

        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)


class UserCreateService(views.APIView):

    def post(self, request):
        password = request.data.get('password')
        user = UserRepository().create_user(request.data, password)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
