from django.conf.urls import url
from django.contrib import admin
from .views import ( goal_list, goal_create, goal_detail, goal_update, goal_delete)

urlpatterns = [
    url(r'^$', goal_list, name="list"),
    url(r'^create/', goal_create),
    url(r'^(?P<id>\d+)/$', goal_detail, name="detail"),
    url(r'^(?P<id>\d+)/edit/', goal_update),
    url(r'^(?P<id>\d+)/delete/', goal_delete),	
]
