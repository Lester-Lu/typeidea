from django.contrib import admin
from .models import Link, SideBar


# Register your models here.


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'weight', 'created_time')
    fields = [ 'title', 'url', 'weight',]

    search_fields = ['title']

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(LinkAdmin, self).save_model(request, obj, form, change)


@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_type', 'created_time', 'status')
    fields = ['title', 'display_type',  'status','content']

    search_fields = ['title','display_type']

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(SideBarAdmin, self).save_model(request, obj, form, change)
