from blog_main_part.models import Category, Post
from django import template

# 实例化一个模板库，给python函数提供装饰器，使之能使用模板标签语法
register = template.Library()


@register.simple_tag  # 这样这个函数就能在模板中用便签语法了（ {%  %} )
def get_recent_posts(num=5):
    """一个获取数据中前num篇文章的函数，提供给模板标签，做文章侧边栏列表"""
    return Post.objects.all()[:num]


@register.simple_tag  # 如法炮制
def archives():
    """通过时间归档列表"""
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag  # 如法炮制
def get_categories():
    """给归档的列表分类"""
    return Category.objects.all()
