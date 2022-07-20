from django.conf.urls import url
from django.contrib.auth.views import LoginView
#from django.contrib.auth import login
from django.urls import path, re_path

from . import views

app_name = 'users'
urlpatterns = [
        #login
        re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name = 'login'),
        re_path(r'^logout/$', views.logout_view, name='logout'),
        re_path(r'^register/$', views.register, name='register'),
]
