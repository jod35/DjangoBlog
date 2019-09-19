from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.


posts=[
    {
        'author':"Ssali Jonathan",
        'title':"Post One",
        'content':" Post Content",
        'date_posted':"17th September 2019" 
    },
    {
        'author':"Kaweesa Andrew",
        'title':"Post Two",
        'content':" Post Content",
        'date_posted':"18th September 2019" 
    }
]
def home(request):
    context={
        'posts' : posts
    }
    return render(request,'blog/index.html',context=context)

def about(request):
    context={
        'title': "About Page",
        'posts' : posts
    }
    return render(request,'blog/about.html',context)

