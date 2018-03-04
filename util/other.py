# encoding: utf-8
# !/usr/bin/env python
# __author__ = "yang"
# Date: 2017/8/25
import os
import pickle

import re


def get_obj_from_pickle(filepath):
    with open(filepath, "rb") as f:
        obj = pickle.load(f)
        return obj


def lianxu(l):
    j = 0
    for i in l:
        j += 1
        if j == i.id:
            pass
        else:
            j += 1
            if j == i.id:
                print("不连续", i.id)
            else:
                j += 1
                if j == i.id:
                    print("不连续", i.id)


def coordinate(Vocabularycet4):
    """将数据库中索引不连续处理为连续"""
    for i in range(1, 1131):
        obj = Vocabularycet4.objects.filter(id=i).first()
        last_one = Vocabularycet4.objects.all().last()

        if not obj:
            last_one.id = i
            last_one.save()

        elif obj.id == last_one.id:
            break


def is_the_id_right():
    p = r"(\d+)"
    path = r"D:\dev\django\VocabularyLearning\vocabularyL\static\img\11"
    for i in os.listdir(path):
        ret = re.match(p, i).group(1)
        word = i.split(ret)[1].strip()
        oldname = os.path.join(path, i)
        newname = os.path.join(path, word)
        os.rename(oldname, newname)


if __name__ == '__main__':
    is_the_id_right()
