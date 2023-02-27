import uuid
from typing import Dict

from django.db.models import Q


class BaseRepository:
    def find(self, id: uuid.UUID):
        try:
            return self.model.objects.get(id=id)
        except self.model.DoesNotExist:
            return False

    def find_by_query(self, query):
        return self.model.objects.filter(query)

    def create(self, data: Dict):
        return self.model.objects.create(**data)

    def update(self, id: uuid.UUID, data: Dict, query=Q()):
        self.model.objects.filter(id=id).filter(query).update(**data)
        return self.find(id)

    def remove(self, id: uuid.UUID):
        self.model.objects.filter(id=id).delete()
