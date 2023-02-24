from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

from resources.repositories.comment_repository import CommentRepository
from resources.serializers.comment_serialize import CommentSerializer 


class CommentCreateService(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        comment = CommentRepository().create_comment(request.data, request.user)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
