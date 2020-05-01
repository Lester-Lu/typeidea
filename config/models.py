from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Link(models.Model):
    title = models.CharField(max_length=50, verbose_name="标签")
    url = models.URLField(verbose_name="友链")
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)),
                                         verbose_name="权重", help_text="权重高拍现在前面")
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="创建者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '友情链接'


class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, '显示'),
        (STATUS_HIDE, '隐藏'),
    )

    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最新评论'),
        (4, '最热文章')
    )
    title = models.CharField(max_length=120, verbose_name='标题')
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE, verbose_name='展示类型', blank=True)
    content = models.CharField(max_length=500, blank=True, verbose_name='内容')
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='创建者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEMS, verbose_name='状态')

    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'
