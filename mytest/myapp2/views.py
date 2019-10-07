from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def index(request):
    return HttpResponse("第二个项目")
def pictures(request):
    return render(request,'myapp2/picture.html')