#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/10/29 下午5:10
# @Author  : robinjia
# @Email   : dengshilong1988@gmail.com
import uuid
from datetime import datetime
import os


def get_file_path(instance, filename):
    folder = instance.__class__.__name__.lower() + datetime.now().strftime("/%Y/%m/%d")
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(folder, filename)

