# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app.models import Blog
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def search(request):
    comments = Blog.objects.all().values('id','content')
    return render(request, 'search.html', {"comments": comments})

def main(request):
    return render(request, 'content.html')