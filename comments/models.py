from blog_main_part.models import Post
from django.db import models


class Comment(models.Model):
    """评论应用的数据库模型"""

    # 用户的名字
    name = models.CharField(max_length=100)

    # 用户的邮箱
    email = models.EmailField(max_length=255)

    # 记录用户的个人网站
    url = models.URLField(blank=True)

    # 用户发表的内容
    text = models.TextField()

    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True)

    # 这条评论关联到唯一那篇文章
    post = models.ForeignKey(Post, related_name='comments')

    def __str__(self):
        return self.text[:20] + "..."
