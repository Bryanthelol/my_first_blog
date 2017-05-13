"""这个文件定义应用blog_main_part的具体URL模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.home, name='home'),

    # 文章详情页
    url(r'^post/(?P<my_args>\d+)/$', views.detail, name='detail'),
]
