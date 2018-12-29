from django.conf.urls import url
from . import views
from django.contrib import admin
from blog.views import home,blog_detail

urlpatterns = [
    #http://127.0.0.1:8000/
    url(r'^$',views.home),
    url(r'(?P<blog_id>\d+)$',views.blog_detail),
    #url(r'^cokies$',views.cooki)
    ]