from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.info, name='info'),
    url('^tasks/$', views.tasks, name='tasks'),
    url('^addhosts/$', views.addhosts, name='addhosts'),
    url('^addmodules/$', views.addmodules, name='addmodules'),
    url('^delarg/(?P<arg_id>\d+)/$', views.delarg, name='delarg'),
]