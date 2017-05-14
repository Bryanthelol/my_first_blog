from django import forms

from .models import Comments


class CommentsForms(forms.ModelForm):

    class Meta:
        # 指定这个表单对应Comments模型
        model = Comments

        # 指定要显示的字段
        fields = ['name', 'email', 'url', 'text']

        # 指定了各个字段在前端渲染的输入框类型
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': "你的昵称",
            }),
            'email': forms.TextInput(attrs={
                'placeholder': "邮箱"，
            }),
            'url': forms.TextInput(attrs={
                'placeholder': "个人网址",
            }),
        }
