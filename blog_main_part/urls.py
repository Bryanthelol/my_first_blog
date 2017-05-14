"""这个文件定义应用blog_main_part的具体URL模式"""

from django.conf.urls import url

from . import views

# 告诉 Django 这个URL文件用于这个应用
app_name = 'blog_main_part'

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 文章详情页
    url(r'^post/(?P<my_args>\d+)/$', views.detail, name='detail'),

    # 归档时间的详情页
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',
        views.archives, name='archives'),

    # 文章分类的详情页
    url(r'^category/(?P<my_args>\d+)/$', views.category, name='category'),
]
