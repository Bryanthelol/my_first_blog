from django.db import models


class Article(models.Model):
    """这个模型显示文章"""
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        """把博客文章降序排列(改变上面的属性date_added)"""
        ordering = ['-date_added']

        # 多篇文字显示复数
        verbose_name_plural = "articles"

    def __str__(self):
        """返回模型生成的数据"""
        return self.title
