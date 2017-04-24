from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from ConcertifyApi import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^musicians/$', views.MusicianList.as_view()),
    url(r'^locations/$', views.LocationList.as_view()),
    url(r'^comments/$', views.CommentsList.as_view()),
]