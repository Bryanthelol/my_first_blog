from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    """对文章进行分类的数据模型"""
    name = models.CharField(max_length=100)


class Tag(models.Model):
    """给文章打上标签的数据模型"""
    name = models.CharField(max_length=100)


class Post(models.Model):
    """一篇文章的数据模型"""
    title = models.CharField(max_length=80)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # blank属性意为是否允许为空值
    excerpt = models.CharField(max_length=200, blank=True)

    # 让一篇文章与它的唯一分类关联（一对多）
    category = models.ForeignKey(Category)

    # 一篇文章有多个标签，这些相同的标签页可能对应多篇文章（多对多）
    tags = models.ManyToManyField(Tag, blank=True)

    # 让一篇文章与它的唯一作者关联（一对多）
    author = models.ForeignKey(User)

    class Meta:
        """把博客文章降序排列(改变上面的属性date_added)"""
        ordering = ['-created_time']
        ordering = ['-modified_time']

        # 多篇文字显示复数
        verbose_name_plural = "posts"

    def __str__(self):
        """返回模型生成的数据"""
        return self.title
