from typing import Dict
from django.db import InternalError, DatabaseError
from django.http import Http404, HttpResponseServerError


class BaseRepository:
    def find(self, id, value_list=[]):
        try:
            if len(value_list):
                return self.model.objects.get(id=id).values(*value_list)
            else:
                return self.model.objects.get(id=id)
        except self.model.DoesNotExist:
            raise Http404
        except InternalError:
            return HttpResponseServerError
        except DatabaseError:
            raise Http404
    
    def create(self, data: Dict):
        return self.model.objects.create(**data)
