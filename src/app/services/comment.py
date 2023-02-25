from typing import Dict, List
import uuid
from django.db.models import Q

from app.domain.models.user import User
from app.domain.repositories.comment import CommentRepository
from app.domain.models.comment import Comment


class CommentService:
    def __init__(self, comment_repository: CommentRepository):
       self.comment_repository = comment_repository
       self.model = Comment

    def create_comment(self, data: Dict, user: User) -> Comment:
        data['user']
        comment = self.comment_repository.create(data)
        return comment
    
    def get_comments(self, user: User) -> List[Comment]:
        query = Q(user=user)
        comments = self.comment_repository.find_all(query)
        return comments

    def get_comment(self, id: uuid.UUID) -> Comment:
        query = Q(transfer__public=True, id=id)
        comment = self.comment_repository.find_all(query)
        return comment.first()
    
    def update_comment(self, id :uuid.UUID, data: Dict) -> Comment:
        comment = self.comment_repository.update(id, data)
        return comment
