from django.shortcuts import render
from .models import *
import json
import matplotlib.pyplot as plt
import numpy as np
# Create your views here.
from django.http import HttpResponse,JsonResponse



def index(request):
    list = ['test']
    return render(request, 'myapp/main.html', {"list": list})


def detail(request, num):
    if num == 'test':
        listss=s821.objects.all()
        return render(request, 'myapp/test_tbl.html', {"test_tbl": listss})
    # elif num == 'ajax':
    #     liss=s821.objects.get(pk=240)
    #     date = {"UA":liss.UA, "UB":liss.UB, "UC":liss.UC}
    #     return JsonResponse(date)
    elif num == 'mxy':
        listss=s821.objects.all()
        return render(request, 'myapp/mxy.html', {"test_tbl": listss})
    else:
        return render(request, 'myapp/'+num)

def ajax(request,num):
    liss = s821.objects.get(pk=int(num))
    date = {"UA": liss.UA, "UB": liss.UB, "UC": liss.UC}
    return JsonResponse(date)


def test(request):
    testList = test_tbl.objects.all()
    return render(request, 'myapp/pictures.html')


def test1(request, num):
    test1List = s821.objects.all()
    for test1 in test1List:
        if test1.name == num:
            test_get = test1
    return render(request, 'myapp/messge.html', {"test": test_get})


# def pics(request):
#     pic = picture.objects.all()
#     return (render(request,'myapp/picture.html',{"pic":pic}))
# def picss(request,num):
#     picList = picture.objects.all()
#     for pic1 in picList:
#         if pic1.id == num :
#             pic = pic1.image_path
#             image_date = open(pic, 'rb').read()
#             return (HttpResponse(image_date, content_type="image/jpg"))