from django.contrib import admin
from .models import Comment
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target','nickname','website','email','status','created_time')

    list_filter = ['status','nickname',]

    search_fields = ['target']

