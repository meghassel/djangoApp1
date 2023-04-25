from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def productList (request) :
    return HttpResponse("<h1>test view content</h1>")

def homePage (request) :
    return render(request,'home.html')