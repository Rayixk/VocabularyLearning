import random

from django.shortcuts import render, HttpResponse, redirect
from django.db.models import F, Q
from vocabularyL import models
from django.conf import settings

# 获取配置信息中的Vocabulary
Vocabulary = getattr(models, settings.VOCABULARY)
print(Vocabulary)

print("in view-------------")
daily_quantity = 100  # 每日的数量

recent_word = {"word": None}
task_list = []


# Create your views here.

def get_task():
    """获取任务,包括今天应该学习的和以前最错的那些"""
    start_index = models.UserInfo.objects.filter(name="yang", wordtype=settings.VOCABULARY).first().wordposition
    today_task = Vocabulary.objects.filter(id__range=[start_index + 1, start_index + daily_quantity])
    # for j in today_task:
    #     print(j)
    # print("-" * 100)
    ret = Vocabulary.objects.filter(~Q(is_first_time="ok"), ~Q(is_first_time="cognize"),
                                    id__lt=start_index, ).order_by("score")
    if settings.MODE == "fast":
        tlist = list(today_task)
    else:
        tlist = list(ret)[0:20] + list(today_task)
    for i in tlist:
        print(i)
    return tlist


task_list += get_task()


def index(request):
    word_obj = task_list.pop(0)
    recent_word["word"] = word_obj

    sword = models.Sword.objects.filter(word=word_obj.word).first()
    print("now word:", word_obj)

    return render(request, "index.html", locals())
    # return HttpResponse(" d ")


def yes(request, index):
    if int(index) > models.UserInfo.objects.filter(name="yang", wordtype=settings.VOCABULARY).first().wordposition:
        models.UserInfo.objects.filter(name="yang", wordtype=settings.VOCABULARY).update(wordposition=int(index))
    this_obj = recent_word["word"]

    if this_obj.is_first_time == "yes":  # 说明是第一次出现该单词,且选择了yes,说明很熟悉,以后复习的时候不再出现
        this_obj.is_first_time = "ok"
    else:
        this_obj.score = this_obj.score + 5  # 说明该单词本次测试熟悉,score+5
    this_obj.save()

    if task_list:
        # 展示下一个单词
        word_obj = task_list.pop(0)
        recent_word["word"] = word_obj
        sword = models.Sword.objects.filter(word=word_obj.word).first()
        print("now word:", word_obj)

        return render(request, "index.html", locals())
    else:
        return render(request, "finish.html")


def no(request, index):
    this_obj = recent_word["word"]

    if this_obj.is_first_time == "yes":  # 该单词第一次出现但是不认识
        this_obj.is_first_time = "no"
    this_obj.score = this_obj.score + 1  # 说明该单词本次测试不熟悉,score+1
    this_obj.save()

    # 将该单词再插入任务列表
    if settings.MODE == "fast":
        pass
    else:
        insert_index = random.choice([4, 5, 6, 7, 8, 9, 10])
        task_list.insert(insert_index, this_obj)

    if task_list:
        # 展示下一个单词
        word_obj = task_list.pop(0)
        recent_word["word"] = word_obj
        sword = models.Sword.objects.filter(word=word_obj.word).first()
        print("now word:", word_obj)

        return render(request, "index.html", locals())
    else:
        return render(request, "finish.html")


def ok(request, index):
    """当完全认识一个单词后,将该单词标记为认识,不再出现在后面的复习,集中精力复习不认识的"""
    if int(index) > models.UserInfo.objects.filter(name="yang", wordtype=settings.VOCABULARY).first().wordposition:
        models.UserInfo.objects.filter(name="yang", wordtype=settings.VOCABULARY).update(wordposition=int(index))

    this_obj = recent_word["word"]
    this_obj.is_first_time = "cognize"
    this_obj.save()

    if task_list:
        # 展示下一个单词
        word_obj = task_list.pop(0)
        recent_word["word"] = word_obj
        sword = models.Sword.objects.filter(word=word_obj.word).first()
        print("now word:", word_obj)

        return render(request, "index.html", locals())
    else:
        return render(request, "finish.html")


def goon(request):
    """go on 再来一组"""
    for i in get_task():
        task_list.append(i)

    return redirect("/index/")


def essay(request):
    return render(request, "essay.html")


def wordshow(request):
    return render(request, "wordshow.html")


def add_word_list(request):
    """so easy"""
    # word_list = []
    # with open("高考3500.txt", encoding="utf-8") as f:
    #     for line in f:
    #         word, word_meaning = line.strip().split(" ", maxsplit=1)
    #         word_list.append(models.Vocabulary3500(word=word,meaning=word_meaning))
    # models.Vocabulary3500.objects.bulk_create(word_list)
    # return HttpResponse("...")

    # models.Vocabulary3500.objects.filter().update(is_first_time="yes")
    s = models.Vocabulary3500.objects.filter(id__gt=0).update(score=0)
    return HttpResponse("...")


def test(request):
    import json
    # word_list = models.Vocabulary1575.objects.values("word", "meaning", "memory_method", "upronun", "upronun_url",
    #                                                  "bpronun", "bpronun_url")
    # l = []
    # for word_obj in word_list:
    #     """
    #     word = models.CharFie
    #     meaning = models.Char
    #     memory_method = model
    #     sentence_en = models.
    #     sentence_cn = models.
    #     pronunciation = model
    #     pronunciation_url = m
    #     pronunciation_en = mo
    #     pronunciation_en_url
    #     """
    #     word_dict = {}
    #     word_dict["word"]=word_obj["word"]
    #     word_dict["meaning"]=word_obj["meaning"]
    #     word_dict["memory_method"]=word_obj["memory_method"]
    #     word_dict["pronunciation"]=word_obj["upronun"]
    #     word_dict["pronunciation_url"]=word_obj["upronun_url"]
    #     word_dict["pronunciation_en"]=word_obj["bpronun"]
    #     word_dict["pronunciation_en_url"]=word_obj["bpronun_url"]
    #     l.append(word_dict)
    # f=open("tmp1.txt","w",encoding="utf-8")
    #
    # json.dump(l,f)
    # f.close()

    # ------------------------------------------------------------------

    # word_list = models.Vocabularycet4.objects.all()
    # l = []
    # for word_obj in word_list:
    #     word_dict = {}
    #     word_dict["word"] = word_obj.word
    #     word_dict["meaning"] = word_obj.meaning
    #     word_dict["memory_method"] = word_obj.memory_method
    #     word_dict["pronunciation"] = word_obj.upronun
    #     word_dict["pronunciation_url"] = word_obj.upronun_url
    #     word_dict["pronunciation_en"] = word_obj.bpronun
    #     word_dict["pronunciation_en_url"] = word_obj.bpronun_url
    #     l.append(word_dict)
    # f=open("tmp1_cet4.txt","w",encoding="utf-8")
    #
    # json.dump(l,f)
    # f.close()
    # ------------------------------------------------------------------
    # word_list = models.Vocabularycet6.objects.all()
    # l = []
    # for word_obj in word_list:
    #     word_dict = {}
    #     word_dict["word"] = word_obj.word
    #     word_dict["meaning"] = word_obj.meaning
    #     word_dict["memory_method"] = word_obj.memory_method
    #     word_dict["pronunciation"] = word_obj.upronun
    #     word_dict["pronunciation_url"] = word_obj.upronun_url
    #     word_dict["pronunciation_en"] = word_obj.bpronun
    #     word_dict["pronunciation_en_url"] = word_obj.bpronun_url
    #     l.append(word_dict)
    # f=open("tmp1_cet6.txt","w",encoding="utf-8")
    #
    # json.dump(l,f)
    # f.close()
    #
    # return HttpResponse("...")

    # ------------------------------------------------------------------
    # word_list = models.Vocabulary5500.objects.all()
    # l = []
    # for word_obj in word_list:
    #     word_dict = {}
    #     word_dict["word"] = word_obj.word
    #     word_dict["meaning"] = word_obj.meaning
    #     l.append(word_dict)
    # f=open("tmp1_5500.txt","w",encoding="utf-8")
    #
    # json.dump(l,f)
    # f.close()
    #
    # return HttpResponse("...")

    # ------------------------------------------------------------------
    # word_list = models.Vocabulary3500.objects.all()
    # l = []
    # for word_obj in word_list:
    #     word_dict = {}
    #     word_dict["word"] = word_obj.word
    #     word_dict["meaning"] = word_obj.meaning
    #     l.append(word_dict)
    # f=open("tmp1_3500.txt","w",encoding="utf-8")
    #
    # json.dump(l,f)
    # f.close()

    # ------------------------------------------------------------------
    word_list = models.Sword.objects.all()
    l = []
    for word_obj in word_list:
        word_dict = {}
        word_dict["word"] = word_obj.word
        word_dict["meaning"] = word_obj.meaning
        word_dict["sentence_en"] = word_obj.sentence_en
        word_dict["sentence_cn"] = word_obj.sentence_ch
        l.append(word_dict)
    f=open("tmp1_sword.txt","w",encoding="utf-8")

    json.dump(l,f)
    f.close()

    return HttpResponse("...")
