from django.http import HttpResponse
from django.shortcuts import render

from .models import Article


def home(request):
    """主页，及其数据处理逻辑"""
    post_list = Article.objects.all()  # 获取Article模型的全部数据
    return render(request, 'blog_main_part/home.html', {'post_list': post_list})
