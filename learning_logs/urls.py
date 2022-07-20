
from django.conf.urls import url
from learning_logs import views
from django.urls import re_path, path

app_name = 'learning_log'

urlpatterns = [
	#主页
	re_path(r'^$', views.index, name = 'index'),
	re_path(r'^topics/$', views.topics, name = 'topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),
    re_path(r'^new_topic/$', views.new_topic, name = 'new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    re_path(r'edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
