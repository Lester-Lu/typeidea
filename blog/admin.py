from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Category, Tag, Post
from .adminforms import BlogAdminForm
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin

# Register your models here.

class CategoryPostInline(admin.TabularInline):
    """在分类里直接添加文章"""
    fields = ('title','desc')
    extra = 1 #显示额外多几个可填框
    model = Post #关联的模型



@admin.register(Category,site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):

    '''inlines可实现模型的关联，并在当前模型下编写关联的模型'''
    #inlines = [CategoryPostInline]

    list_display = ('id', 'name', 'status', 'is_nav', 'owner', 'created_time')
    fields = ('name', 'is_nav', 'status',)



    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag,site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('id', 'name', 'status', 'owner', 'created_time')
    fields = ('name', 'status',)



    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'

class CategoryOwnerFilter(admin.SimpleListFilter):
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner = request.user).values_list('id','name')


    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id = self.value())
        return queryset





@admin.register(Post,site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = BlogAdminForm

    list_display = ('id', 'title', 'category', 'status', 'owner', 'created_time', 'operator')

    list_display_links = ['title']

    list_filter = [CategoryOwnerFilter]

    search_fields = ['title', 'category__name']

    # actions_on_top = True
    # actions_on_bottom = True

    # 编辑页面
    # save_on_top = True

    fileds = (
        ('category', 'title'),
        'desc',
        'status',
        'content',
        'tag',
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>', reverse('cus_admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)
