from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import TaskHandler

hndlr = Resource(TaskHandler)

urlpatterns = patterns('',
    ('^tasks/(?P<task_id>[\d]+)', hndlr), 
    ('^tasks', hndlr)    
)


