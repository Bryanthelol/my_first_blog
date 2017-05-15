from blog_main_part.models import Post
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentsForms
from .models import Comments


def post_comment(request, post_args):

    # 获取与评论相关联的那篇文章
    post = get_object_or_404(Post, id=int(post_args))

    # 当用户提交表单（POST）时，才处理表单数据
    if request.method != 'POST':
        # 不是POST请求，说明用户没提交数据，重新定向到详情页
        return redirect(post)

    else:
        # 把数据传入表单模型，并实例化
        form = CommentsForms(request.POST)

        # 检查表单是否符合格式要求
        if form.is_valid():
            # 合法，调用save方法保存，
            # commit=False作用是升舱恒实例，但还不保存到数据库
            comment = form.save(commit=False)
            # 将评论和被评论的文章关联起来
            comment.post = post
            # 最后将评论数据保存近数据库，调用模型实例的save方法
            comment.save()

            # 重定向到post的详情页
            return redirect(post)

        else:
            # 数据不合法，重新渲染详情页，再渲染表单的错误
            # 因为是关联的，post.comment_set.all()获取post下全部评论
            comment_list = post.comment_set.all()
            return render(request, 'blog_main_part/detail.html', {'post'： post,
                                                                  'form': form,
                                                                  'comment_list': comment_list})
