from django.contrib import admin
from django.urls import path, include, re_path
from .views import post_list, post_create, post_update, post_detail

urlpatterns = [
    re_path(r'^$', view = post_list),
    re_path(r'^detail/$', view = post_detail),
    re_path(r'^create/$', view = post_create)
]