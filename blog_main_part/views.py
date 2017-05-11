from django.http import HttpResponse
from django.shortcuts import render

from .models import Article


def home(request):
    """主页，及其数据处理逻辑"""
    post_list = Article.objects.all()  # 获取Article模型的全部数据
    return render(request, 'blog_main_part/home.html', {'post_list': post_list})


def detail(request, my_args):
    """文章详情页，及其数据处理逻辑"""
    post = Article.objects.all()[int(my_args)]
    str = ("title=%s, category=%s, date_added=%s, content=%s"
           % (post.title, post.category, post.date_added, post.content))
    return HttpResponse(str)
