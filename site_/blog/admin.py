from django.contrib import admin
from .models import Article
from .models import Slider
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name','date','title', 'body', 'timestamp','image']

admin.site.register(Article, ArticleAdmin)

class SliderAdmin(admin.ModelAdmin):
    list_display = ['image']

admin.site.register(Slider,SliderAdmin)