import uuid
from typing import Dict

from django.db.models import Q
from django.db import InternalError, DatabaseError
from django.http import Http404, HttpResponseServerError


class BaseRepository:
    def find(self, id: uuid.UUID):
        try:
            return self.model.objects.get(id=id)
        except self.model.DoesNotExist:
            raise Http404
        except InternalError:
            return HttpResponseServerError
        except DatabaseError:
            raise Http404
    
    def find_all(self, query):
        return self.model.objects.filter(query)
    
    def create(self, data: Dict):
        return self.model.objects.create(**data)

    def update(self, id: uuid.UUID, data: Dict, query=Q()):
        self.model.objects.filter(id=id).filter(query).update(**data)
        return self.find(id)
