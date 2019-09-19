from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello Home</h1>")

def about(request):
    return HttpResponse('<h1>This is the About Page</h1>')