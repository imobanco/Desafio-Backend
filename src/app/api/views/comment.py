from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.permissions import OwnProfilePermission

from app.services.comment import CommentService
from app.domain.repositories.comment import CommentRepository
from app.api.serializers.comment import CommentSerializer


class CommentCreateView(views.APIView):
    permission_classes = (IsAuthenticated,)
    service = CommentService(CommentRepository())
    serializer_class = CommentSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            comment = self.service.post_comment(
                serializer.validated_data,
                request
                )
            serializer = self.serializer_class(comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        comments = self.service.get_comments(request)
        serializer = self.serializer_class(comments, many=True)
        return Response(serializer.data)


class CommentDetailsView(views.APIView):
    permission_classes = (IsAuthenticated, OwnProfilePermission)
    service = CommentService(CommentRepository())
    serializer_class = CommentSerializer

    def get(self, request, id):
        comment = self.service.get_comment(id=id)
        serializer = self.serializer_class(comment)
        return Response(serializer.data)

    def patch(self, request, id):
        comment = self.service.put_comment(id, request)
        serializer = self.serializer_class(comment)
        return Response(serializer.data)
