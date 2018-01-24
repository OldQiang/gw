from django.shortcuts import render
from django.http import  HttpResponse
from .models import Article
import os
# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def upload(request):
    return render(request,'upload.html')

def blog_index(request):
    blog_list = Article.objects.all() # 获取所有数据
    return render(request,'index.html', {'blog_list':blog_list})