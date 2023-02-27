from typing import Dict, List
import uuid
from django.db.models import Q

from app.domain.repositories.base import BaseRepository

from app.domain.models.comment import Comment
from app.domain.models.user import User


class CommentRepository(BaseRepository):
    def __init__(self) -> None:
        self.model = Comment

    def create_comment(self, data: Dict, user: User) -> Comment:
        data["user"] = user
        comment = self.create(data)

        return comment

    def find_comments(self, user: User) -> List[Comment]:
        comments = self.find_by_query(Q(user=user))
        return comments

    def find_comment(self, id: uuid.UUID) -> Comment:
        comment = self.find_by_query(Q(transfer__public=True, id=id))
        return comment.first()
