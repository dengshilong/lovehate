#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/10/30 下午1:13
# @Author  : robinjia
# @Email   : dengshilong1988@gmail.com

from django.conf.urls import url
from .views import UserLogin, register

urlpatterns = [
    url(r'^login$', UserLogin.as_view(), name='user_login'),
]