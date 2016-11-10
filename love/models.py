from uuid import uuid4
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from user.models import User
from common.utils import get_file_path

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        db_table = 'category'
        verbose_name = verbose_name_plural = '类别'


class Post(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, verbose_name='创建者')
    cover = models.ImageField(verbose_name='图片', upload_to=get_file_path)
    cover_thumbnail = ImageSpecField(source='cover',
                                     processors=[ResizeToFill(400, 400)],
                                     format='JPEG',)
    create_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name='类别')

    def __str__(self):
        return '{}'.format(self.uuid)

    class Meta:
        db_table = 'post'
        verbose_name = verbose_name_plural = 'post'
