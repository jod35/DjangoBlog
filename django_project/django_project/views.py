from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("<h1>About</h1>")

def services(request):
    return HttpResponse("<h1>Services</h1>")