# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class blog_article(models.Model):
    author=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    title=models.CharField(max_length=100)
    content=models.TextField()
    image=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

