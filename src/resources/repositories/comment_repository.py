from typing import Dict, List
import uuid
from django.db.models import Q

from resources.repositories.base_repository import BaseRepository

from resources.models import Comment, User


class CommentRepository(BaseRepository):
    def __init__(self) -> None:
        self.model = Comment

    def create_comment(self, data: Dict, user: User) -> Comment:
        data['user'] = user
        comment = self.create(data)
        
        return comment
