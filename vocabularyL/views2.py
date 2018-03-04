import random

from django.shortcuts import render, HttpResponse, redirect
from django.db.models import F, Q
from vocabularyL.models import *
import json
import copy

print("in view2-------------")
daily_quantity = 30  # 每日的数量

recent_word = {"word": None}
task_list = []


def get_task():
    """获取任务,包括今天应该学习的和以前最错的那些"""
    start_index = UserInfo.objects.filter(name="yang").first().wordposition
    today_task = Vocabulary1575.objects.filter(id__range=[start_index + 1, start_index + daily_quantity])
    # for j in today_task:
    #     print(j)
    # print("-" * 100)
    ret = Vocabulary1575.objects.filter(~Q(is_first_time="ok"), ~Q(is_first_time="cognize"),
                                        id__lt=start_index, ).order_by("score")
    Tlist = list(ret)[0:30] + list(today_task)
    for i in Tlist:
        print(i)
    return Tlist


task_list += get_task()


def wordshow(request):
    if not task_list:
        return redirect("/done/")
    word_list = []
    if len(task_list) < 8:
        word_list = copy.deepcopy(task_list)
        task_list.clear()
    else:
        for i in range(8):
            word_list.append(task_list.pop(0))
    word_list = parse_list(word_list)

    print("len in wordshow:", len(task_list))
    return render(request, "wordshow.html", locals())


def parse_list(l):
    d = {}
    for i in l:
        d[i] = Sword.objects.filter(word=i.word).first()
    return d


def reply(request):
    """处理前端返回回来的单词的yes或no"""
    statue = request.GET.get("statue")
    word_id = request.GET.get("word_id")
    word_obj = Vocabulary1575.objects.get(id=int(word_id))
    if statue == "no":
        if word_obj.is_first_time == "yes":  # 该单词第一次出现但是不认识
            word_obj.is_first_time = "no"
        word_obj.score = word_obj.score + 1  # 说明该单词本次测试不熟悉,score+1

        # 将该单词再插入任务列表
        insert_index = random.choice([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        task_list.insert(insert_index, word_obj)
    else:
        # 同步进度
        if int(word_id) > UserInfo.objects.filter(name="yang").first().wordposition:
            UserInfo.objects.filter(name="yang").update(wordposition=int(word_id))

        if word_obj.is_first_time == "yes":  # 说明是第一次出现该单词,且选择了yes,说明很熟悉,以后复习的时候不再出现
            word_obj.is_first_time = "ok"
        else:
            word_obj.score = word_obj.score + 5  # 说明该单词本次测试熟悉,score+5
    print(word_obj)
    word_obj.save()
    print("len in reply:", len(task_list))
    return HttpResponse("OK")


def shownext(request):
    """下一页,后八个单词"""
    if not task_list:
        return redirect("/done/")
    word_list = []
    if len(task_list) < 8:
        word_list = copy.deepcopy(task_list)
        task_list.clear()
    else:
        for i in range(8):
            word_list.append(task_list.pop(0))
    word_list = parse_list(word_list)
    print("len in shownext:", len(task_list))
    return render(request, "wordshow.html", locals())


def retry(requset):
    """再来一组"""
    for i in get_task():
        task_list.append(i)

    return redirect("/wordshow/")


def done(request):
    word_list = []
    empty = True
    return render(request, "wordshow.html", locals())


def edit(request):
    """词汇信息编辑"""

    return render(request, "word_edit.html")


def search(request):
    """搜索"""
    keyword = request.GET.get("keyword")
    condition = request.GET.get("condition")
    if condition == "indistinct":  # 模糊搜索
        res = Vocabulary1575.objects.filter(word__contains=keyword)[:10]
        l = []
        for i in res:
            l.append(i.word + "  " + the_trim(i.meaning))
        return HttpResponse(json.dumps(l))
    elif condition == "exactly":  # 精确搜索
        word_obj = Vocabulary1575.objects.filter(word=keyword).first()
        if word_obj:
            res = get_word_info(word_obj)
            return HttpResponse(json.dumps(res))
        else:
            return HttpResponse("none")


def the_trim(s):
    """音标,类似 [əˈtendənt]"""

    if "[" in s and "]" in s:
        return s[s.find("]") + 1:]
    else:
        return s


def get_word_info(word_obj):
    d = {}
    d["word"] = word_obj.word
    d["meaning"] = word_obj.meaning
    d["memory_method"] = word_obj.memory_method
    sword_obj = Sword.objects.filter(word=word_obj.word).first()
    d["sentence_en"] = sword_obj.sentence_en if sword_obj else " "
    d["sentence_cn"] = sword_obj.sentence_ch if sword_obj else " "
    return d


def save(request):
    """保存前端回传的单词信息"""
    word = request.POST.get("word")
    meaning = request.POST.get("meaning")
    memory_method = request.POST.get("memory_method")
    sentence_en = request.POST.get("sentence_en")
    sentence_cn = request.POST.get("sentence_cn")
    Vocabulary1575.objects.filter(word=word).update(meaning=meaning, memory_method=memory_method)

    if Sword.objects.filter(word=word):
        Sword.objects.filter(word=word).update(sentence_en=sentence_en, sentence_ch=sentence_cn)
    else:
        Sword.objects.create(word=word,sentence_en=sentence_en, sentence_ch=sentence_cn)
    return HttpResponse("Save OK")
