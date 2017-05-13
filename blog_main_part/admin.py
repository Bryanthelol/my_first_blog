# Register your models here.
from django.contrib import admin

from .models import Category, Post, Tag


class PostAdmin(admin.ModelAdmin):
    """在后台显示更详细的文章相关信息"""
    list_display = ['title', 'created_time',
                    'modified_time', 'category', 'author']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
