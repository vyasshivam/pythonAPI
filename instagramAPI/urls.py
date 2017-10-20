# -*- coding: utf-8 -*-

from django.conf.urls import url
from instagramAPI import views

urlpatterns = [
        #http://127.0.0.1:8000/insta/insta/userName
    url(r'^insta/(?P<userName>.+)/$', views.getInstaPic),
]