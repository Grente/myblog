# coding: utf-8
from app.models import Blog
from django.http import HttpResponse
from django.shortcuts import render

def search(request):
    comments = Blog.objects.all().values('id','content')
    return render(request, 'search.html', {"comments": comments})