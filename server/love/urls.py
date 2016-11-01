#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/10/29 下午9:04
# @Author  : robinjia
# @Email   : dengshilong1988@gmail.com


from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import CreatePost, Index

urlpatterns = [
    url(r'^$', Index.as_view(), name='post_index'),
    url(r'^add/?$', login_required(CreatePost.as_view(), login_url='/login'), name='post_create'),
]


