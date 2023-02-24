from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

from api.permissions import OwnProfilePermission
from resources.repositories.comment_repository import CommentRepository
from resources.serializers.comment_serialize import CommentSerializer 


class CommentCreateService(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        comment = CommentRepository().create_comment(request.data, request.user)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def get(self, request):
        comment = CommentRepository().get_comments(request.user)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)


class CommentDetailsService(views.APIView):
    permission_classes = (IsAuthenticated, OwnProfilePermission)

    def get(self, request, id):
        comment = CommentRepository().get_comment(id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def patch(self, request, id):
        comment = CommentRepository().update_comment(id, request.data)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)