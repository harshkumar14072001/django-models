from django.shortcuts import render
from .models import *
from django.http import *
def index(request):
    d=post.objects.all()
    for i in d:
         print(i.title)
    #return HttpResponse("asd")     
# Create your views here.
