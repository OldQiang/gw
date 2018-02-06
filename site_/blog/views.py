from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponse
from .models import *
from markdown import markdown
from django.http import Http404
from .forms import CommentForm

import os
# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def upload(request):
    return render(request,'upload.html')

def test(request):
    return render(request,'test.html')

def blog_index(request):
    blog_list = Article.objects.all() # 获取所有数据

    for blog in blog_list:
        blog.body = markdown( blog.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    slider_list =  Slider.objects.all();
    return render(request,'index.html', {'blog_list':blog_list},{'slider_list':slider_list})

def blog_details(request,blog_id):
    try:
        blog = Article.objects.get(id=blog_id)
        blog.body = markdown( blog.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    except Article.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['Article'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog':blog,
        'comments':blog.comment_set.all().order_by('-created'),
        'form':form
    }
    return render(request,'details.html',ctx)