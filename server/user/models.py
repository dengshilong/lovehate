# coding: utf-8
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from datetime import datetime
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self,nick, password=None,**extra_fields):
        """
        创建一个用户，账号，和密码
        """
        now = datetime.now()
        if not nick:
            raise ValueError(u'必须填写昵称')
        user = self.model(nick=nick,create_time=now,update_time=now,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,nick, password,**extra_fields):
        """
        创建一个超级用户
        """
        u = self.create_user(nick=nick,password=password,**extra_fields)
        u.is_staff = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class User(AbstractBaseUser,PermissionsMixin):
    nick = models.CharField('昵称', max_length=30, unique=True)
    mobile = models.CharField('手机号',max_length=20, blank=True)
    is_staff = models.BooleanField('是否内部人员', default=False)
    create_time = models.DateTimeField('注册时间', auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'nick'

    objects = MyUserManager()

    class Meta:
        db_table = 'user'
        verbose_name = verbose_name_plural = '用户'

    def get_full_name(self):
        return self.nick

    def get_short_name(self):
        return self.nick