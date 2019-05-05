# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(verbose_name='标题', max_length=48)
    author = models.CharField(verbose_name='作者', max_length=16)
    content = RichTextField(verbose_name='正文', default='')
    create_time = models.DateField(verbose_name='时间', auto_now=True)

    class Meta(object):
        verbose_name = '我的博客'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title