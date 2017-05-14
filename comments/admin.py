from django.contrib import admin

from .models import Comments


class CommentsAdmin(admin.ModelAdmin):
    """在后台显示更详细的评论信息"""
    list_display = ['name', 'created_time', 'text'[:50]]


admin.site.register(Comments, CommentsAdmin)
