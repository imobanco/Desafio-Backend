from typing import Dict
import uuid
from django.db import InternalError, DatabaseError
from django.http import Http404, HttpResponseServerError


class BaseRepository:
    def find(self, id):
        try:
            return self.model.objects.get(id=id)
        except self.model.DoesNotExist:
            raise Http404
        except InternalError:
            return HttpResponseServerError
        except DatabaseError:
            raise Http404
    
    def find_all(self, query):
        return self.model.objects.filter(**query)
    
    def create(self, data: Dict):
        return self.model.objects.create(**data)

    def update(self, id: uuid.UUID, data: Dict):
        self.model.objects.filter(id=id).update(**data)
        return self.find(id)
        
