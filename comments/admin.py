from django.contrib import admin

from .models import Comment


class CommentsAdmin(admin.ModelAdmin):
    """在后台显示更详细的评论信息"""
    list_display = ['name', 'created_time', 'post', 'text'[:50]]


admin.site.register(Comment, CommentsAdmin)
