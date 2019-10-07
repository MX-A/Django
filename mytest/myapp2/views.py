from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import *
from .read_data import read_data
# Create your views here.
def index(request):
    return render(request,"myapp2/main.html")
def pictures(request):
    return render(request,'myapp2/picture.html')
def ajax(request):
    # try:
    UA,UB,UC,IA,IB,IC = read_data()#数据是从read_data函数得到的
    # save_date(UA,UB,UC,IA,IB,IC)
    date = {"UA": UA, "UB": UB, "UC": UC, "IA": IA, "IB": IB, "IC": IC}
    return JsonResponse(date)