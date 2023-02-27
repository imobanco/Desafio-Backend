from typing import List
import uuid
from rest_framework.request import Request

from app.domain.repositories.comment import CommentRepository
from app.domain.models.comment import Comment


class CommentService:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository
        self.model = Comment

    def post_comment(self, request: Request) -> Comment:
        data = request.data
        data["user"] = request.user
        comment = self.comment_repository.create(data)
        return comment

    def get_comments(self, request: Request) -> List[Comment]:
        comments = self.comment_repository.find_comments(request.user)
        return comments

    def get_comment(self, id: uuid.UUID) -> Comment:
        comment = self.comment_repository.find_comment(id)
        return comment

    def put_comment(self, id: uuid.UUID, request: Request) -> Comment:
        comment = self.comment_repository.update(id, request.data)
        return comment
