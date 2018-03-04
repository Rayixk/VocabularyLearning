# encoding: utf-8
# !/usr/bin/env python
# __author__ = "yang"
# Date: 2017/8/25

from django import template

register = template.Library()


@register.filter
def addpng(name,suffix):
    return "img/"+name + suffix
