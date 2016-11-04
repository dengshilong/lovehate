#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/10/29 下午9:04
# @Author  : robinjia
# @Email   : dengshilong1988@gmail.com


from django.conf.urls import url

from .views import PostCreate, Index, CategoryList

urlpatterns = [  # pylint: disable=C0103
    url(r'^$', Index.as_view(), name='index'),
    url(r'^add/?$', PostCreate.as_view(), name='post_create'),
    url(r'^category/(?P<category>\w+)/?$',
        CategoryList.as_view(), name='post_category'),

]
