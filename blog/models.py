
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    name = models.CharField(max_length=50,verbose_name="名称")
    status = models.PositiveIntegerField(default= STATUS_NORMAL,choices = STATUS_ITEMS, verbose_name="分类")
    is_nav = models.BooleanField(default=False,verbose_name="是否为导航")
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="创建者")
    created_time  = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '分类'


    def __str__(self):
        return self.name

    def __int__(self):
        return self.status



class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    name = models.CharField(max_length=50,verbose_name = "名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices = STATUS_ITEMS,verbose_name="状态")
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name = "创建者")
    created_time = models.DateTimeField(auto_now_add = True , verbose_name= "创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '标签'


    def __str__(self):
        return self.name


    def __int__(self):
        return self.status


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
        (STATUS_DRAFT,'草稿'),
    )
    title = models.CharField(max_length=120,verbose_name="标题")
    desc = models.CharField(max_length=1024,verbose_name="摘要",blank=True)
    content = models.TextField(verbose_name= "内容")
    status = models.PositiveIntegerField(default = STATUS_DRAFT,choices=STATUS_ITEMS,verbose_name='状态')
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    tag = models.ForeignKey(Tag,on_delete=models.DO_NOTHING,verbose_name="标签")

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']

    def __str__(self):
        return self.title

    def __int__(self):
        return self.status

    @classmethod
    def get_all_post(cls):
        #cls.objetcs.raw('select * from blog_post')
        pass
