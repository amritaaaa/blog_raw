# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from django.shortcuts import HttpResponse
from django.shortcuts import render
from  . import models
from blog.models import blog_article


# Create your views here.
def home(request):
    article=models.blog_article.objects.all()
    context={
        "article":article

    }
    return render(request,'home.html',context)

def blog_detail(request,blog_id):
    obj=models.blog_article.objects.filter(id=blog_id)
    context={
        'obj':obj
    }
    return render(request,'blog_detail.html',context)

#def cooki(request):
   # create cookies()'''



