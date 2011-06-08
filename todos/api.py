from tastypie.resources import ModelResource
from todos.models import Task 

class TaskResource(ModelResource):
    class Meta:
        queryset = Todo.objects.all()

