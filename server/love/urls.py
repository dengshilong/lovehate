#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/10/29 下午9:04
# @Author  : robinjia
# @Email   : dengshilong1988@gmail.com


from django.conf.urls import url
from .views import CreatePost, Index

urlpatterns = [
    url(r'/', Index.as_view(), name='post_index'),
    url(r'^add/', CreatePost.as_view(), name='post_create'),
]


