from django.shortcuts import render
from .models import *
from .read_data import read_data
from .save_data import save_date
import json
import matplotlib.pyplot as plt
import numpy as np
# Create your views here.
from django.http import HttpResponse,JsonResponse



def index(request):
<<<<<<< HEAD
    return render(request, 'myapp/main.html')

def realtimedata(request):
    return render(request,'myapp/realtimedate.html')
def historydata(request):
    datalist=s821.objects.all()
    return render(request,'myapp/historydate.html',{"datelist":datalist})
# def detail(request, num):
#     if num == 'test':
#         listss=s821.objects.all()
#         return render(request, 'myapp/test_tbl.html', {"test_tbl": listss})
#     # elif num == 'ajax':
#     #     liss=s821.objects.get(pk=240)
#     #     date = {"UA":liss.UA, "UB":liss.UB, "UC":liss.UC}
#     #     return JsonResponse(date)
#     elif num == 'mxy':
#         listss=s821.objects.all()
#         return render(request, 'myapp/mxy.html', {"test_tbl": listss})
#     else:
#         return render(request, 'myapp/'+num)

def ajax(request):
    # try:
    UA,UB,UC,IA,IB,IC = read_data()#数据是从read_data函数得到的
    # save_date(UA,UB,UC,IA,IB,IC)
    print('succss join')
=======
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
    # try:
    UA,UB,UC,IA,IB,IC = read_data()
    # save_date(UA,UB,UC,IA,IB,IC)
>>>>>>> bb3aec808e56180721e4de7bb1a087c949da3d79
    date = {"UA": UA, "UB": UB, "UC": UC,"IA":IA,"IB":IB,"IC":IC}
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