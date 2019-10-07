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
    return render(request, 'myapp/main.html')
def realtimedata(request):
    return render(request,'myapp/realtimedate.html')
def historydata(request):
    datalist=s821.objects.all()
    return render(request,'myapp/historydate.html',{"datelist":datalist})
def ajax(request):
    # try:
    UA,UB,UC,IA,IB,IC = read_data()#数据是从read_data函数得到的
    # save_date(UA,UB,UC,IA,IB,IC)
    date = {"UA": UA, "UB": UB, "UC": UC, "IA": IA, "IB": IB, "IC": IC}
    return JsonResponse(date)