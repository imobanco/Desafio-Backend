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
        data['user'] = user
        comment = self.create(data)
        
        return comment
    
    def get_comments(self, user: User) -> List[Comment]:
        query = Q(user=user)
        comments = self.find_all(query)
        return comments

    def get_comment(self, id: uuid.UUID) -> Comment:
        query = Q(transfer__public=True, id=id)
        comment = self.find_all(query)
        return comment.first()
    
    def update_comment(self, id :uuid.UUID, data: Dict) -> Comment:
        comment = self.update(id, data)
        return comment
