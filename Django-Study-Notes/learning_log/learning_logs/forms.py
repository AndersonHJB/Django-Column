# -*- coding: utf-8 -*-
# @Time    : 2023/3/26 00:30
# @Author  : AI悦创
# @FileName: forms.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic  # """用户学习的主题"""
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ' '}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
