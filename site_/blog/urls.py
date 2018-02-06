from django.conf.urls import url
from . import  views,upload_file,forms

urlpatterns = [
 #   url(r'^$',views.index,name='index'),
    url(r'^upload$',views.upload,name='upload'),
    url(r'^upload_file$', upload_file.upload_file ),
    url(r'^$', views.blog_index,name = 'blog_index'),
    url(r'^test$', views.test),
    url(r'^detail/(\d+)/$',views.blog_details ,name='blog_get_detail'),
]