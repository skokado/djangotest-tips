from django.db import models

from account.models import User


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='投稿者',
                               null=True, on_delete=models.SET_NULL)
    title = models.CharField('件名', max_length=127)
    body = models.TextField('本文', null=True, default='')
