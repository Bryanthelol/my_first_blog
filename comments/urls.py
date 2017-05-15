from django.conf.urls import url

from . import views

app_name = 'comments'

urlpatterns = [
    url(r'^comment/post/(?P<post_args>\d+)/$',
        views.post_comment, name='post_comment'),
]