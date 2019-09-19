from django.shortcuts import render
from  django.http import HttpResponse
from .models import Post
# Create your views here.

def home(request):
    context={
        'posts' : Post.objects.all()
    }
    return render(request,'blog/index.html',context=context)

def about(request):
    context={
        'title': "About Page",
        'posts' : posts
    }
    return render(request,'blog/about.html',context)

