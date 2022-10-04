from django.shortcuts import render
from django.http import *
import datetime
def index(request):
    #return HttpResponse("hello world")
    d=[1,2,3,4]
    f={"info":d}
    return render(request,'index.html',f)
def second(request):
     dt=datetime.datetime.today().time()
     k={"time":dt}
     return render(request,"second.html",k)
         
