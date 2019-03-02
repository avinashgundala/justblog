from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    post = Post.objects.all()
    content = {
            'post':post
    }
    return render(request,'blog/home.html',content)

def about(request):
    return render(request,'blog/about.html')
