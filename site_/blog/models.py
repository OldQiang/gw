from django.db import models

# Create your models here.

class Catagory(models.Model):
    name = models.CharField('名称',max_length=30,default=0)
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('名称',max_length=16,default=0)
    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('标题',max_length=128,default=0)  # 博客标题
    author = models.CharField('作者', max_length=16,default=0)
    abstract = models.TextField('摘要', max_length=200, default=0)
    body = models.TextField('正文',max_length=65536,default=0) # 博客正文
    timestamp = models.DateTimeField('时间',default=0) # 创建时间
    image = models.ImageField(upload_to='static/images/',default=0)#图片
#    catagory = models.ForeignKey(Catagory,verbose_name='分类',on_delete=models.CASCADE,default=0)
#    tags = models.ManyToManyField(Tag,verbose_name='标签',default=0)
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Article, verbose_name='博客',on_delete=models.CASCADE,default=0)
    name = models.CharField('称呼',max_length=16,default=0)
    email = models.EmailField('邮箱',default=0)
    content = models.CharField('内容',max_length=240,default=0)
    created = models.DateTimeField('发布时间',default=0)
    def __unicode__(self):
        return self.content

class Slider(models.Model):
    image = models.ImageField('幻灯片',upload_to='static/images/',default=0)#幻灯片图片
