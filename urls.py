from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
        ('^$', direct_to_template, {'template': 'index.html'}),
        ('^api/', include('api.urls'))
)
