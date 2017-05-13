import markdown
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import cache_page

from .models import Post


# @cache_page(60 * 15) 对单个视图函数使用缓存（暂不使用）
def index(request):
    """主页，及其数据处理逻辑"""
    post_list = Post.objects.all()  # 获取Post数据模型的全部数据
    return render(request, 'blog_main_part/index.html', {'post_list': post_list})


def detail(request, my_args):
    """文章详情页，及其数据处理逻辑"""
    post = get_object_or_404(Post, id=int(my_args))
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog_main_part/detail.html', {'post': post})
