import markdown
from comments.forms import CommentsForms
from django.shortcuts import get_object_or_404, render
from django.utils.text import slugify
from django.views.decorators.cache import cache_page
from markdown.extensions.toc import TocExtension

from .models import Category, Post


# @cache_page(60 * 15) 对单个视图函数使用缓存（暂不使用）
def index(request):
    """主页，及其数据处理逻辑"""
    post_list = Post.objects.all()  # 获取Post数据模型的全部数据
    return render(request, 'blog_main_part/index.html', {'post_list': post_list})


def detail(request, my_args):
    """文章详情页，及其数据处理逻辑"""
    post = get_object_or_404(Post, id=my_args)
    post.increase_views()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify)])  # slugify参数处理中文锚值显示问题
    post.body = md.convert(post.body)  # 用convert方法将markdown文本渲染成html
    form = CommentsForms()
    # 获取这篇post下的全部评论
    comment_list = post.comments.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list,
               'toc': md.toc}  # 一旦调用convert方法后，md就会多出一个toc属性

    return render(request, 'blog_main_part/detail.html', context=context)


def archives(request, year, month):
    """归档时间详情页"""

    # created_time.year，这个实例调用属性，但由于这里做参数，故改为两个下划线 __
    post_list = Post.objects.filter(
        created_time__year=year, created_time__month=month)
    return render(request, 'blog_main_part/index.html', {'post_list': post_list})


def category(request, my_args):
    """文章分类的详情页"""
    cate = get_object_or_404(Category, id=my_args)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog_main_part/index.html', {'post_list': post_list})
