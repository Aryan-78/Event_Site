from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "frame/index.html")

def contact(request):
    return render(request,"frame/contact.html")

def elements(request):
    return render(request,'frame/elements.html')

def eventsnews(request):
    return render(request, 'frame/events-news.html')

def events(request):
    return render(request, 'frame/events.html')

def qwer(request):
    return render(request, 'frame/qwer.html')

def singleevent(request):
    return render(request, 'frame/single-event.html')