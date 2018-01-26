from django.contrib import admin
from .models import *

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','abstract', 'body', 'timestamp','image']

admin.site.register(Article, ArticleAdmin)

class SliderAdmin(admin.ModelAdmin):
    list_display = ['image']

admin.site.register(Slider,SliderAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Tag,TagAdmin)

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Catagory, CatagoryAdmin)
