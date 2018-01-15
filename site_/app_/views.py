from django.shortcuts import render,HttpResponse
from app_.models import People

# Create your views here.

def data_base_test(request):
    someone = People(name='bro',password='666666')
    return HttpResponse('hello '+someone.name)