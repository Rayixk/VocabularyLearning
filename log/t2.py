# encoding: utf-8
# !/usr/bin/env python
# __author__ = "yang"
# Date: 2017/8/29
task=[]

def foo():
    l = [3, 4, 5, 6, 7]
    return l


task =task+foo()


def foo2():
    l = [3, 4]
    return l


def fun():
    for i in foo2():
        task.append(i)


if __name__ == '__main__':
    fun()
    print(task)
