from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import Category, Post, Tag


@cache_page(60 * 15)
def home(request):
    """主页，及其数据处理逻辑"""
    post_list = Post.objects.all()  # 获取Post数据模型的全部数据
    return render(request, 'blog_main_part/index.html', {'post_list': post_list})


@cache_page(60 * 15)
def detail(request, my_args):
    """文章详情页，及其数据处理逻辑"""
    post = Post.objects.get(id=int(my_args))
    return render(request, 'blog_main_part/detail.html', {'post': post})
