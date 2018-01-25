from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=256,default=0)
    date = models.DateTimeField(max_length=128,default=0)
    title = models.CharField(max_length=150,default=0)  # 博客标题
    body = models.TextField(max_length=65536,default=0) # 博客正文
    timestamp = models.DateTimeField(max_length=32,default=0) # 创建时间
    image = models.ImageField(upload_to='../static/images/',default=0)#图片

class Slider(models.Model):
    image = models.ImageField(upload_to='../static/images/',default=0)#幻灯片图片