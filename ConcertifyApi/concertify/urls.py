from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from ConcertifyApi import views

urlpatterns = [
    # URLs for User class
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    # URLs for Musician class
    url(r'^musicians/$', views.MusicianList.as_view()),
    url(r'^musicians/(?P<pk>[0-9]+)/$', views.MusicianDetail.as_view()),

    # URLs for Location class
    url(r'^locations/$', views.LocationList.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/$', views.LocationDetail.as_view()),

    # URLs for Concert class
    url(r'^concerts',views.ConcertList.as_view()),

    # URLs for Tag class
    url(r'^tags/$', views.TagList.as_view()),

    # URLs for MainHall class
    url(r'^mainhalls/$', views.MainHallList.as_view()),
    # URLs for comments
    url(r'^comments/$', views.CommentsList.as_view()),

]
