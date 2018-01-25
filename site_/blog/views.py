from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponse
from .models import Article,Slider
from markdown import markdown
import os
# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def upload(request):
    return render(request,'upload.html')

def blog_index(request):
    blog_list = Article.objects.all() # 获取所有数据
    for blog in blog_list:
        blog.body = markdown(blog.body)
    slider_list =  Slider.objects.all();
    for slider in slider_list:
        print("slider.image url is ")
        print(slider.image)
        print(slider.image.url)
    return render(request,'index.html', {'blog_list':blog_list},{'slider_list':slider_list})