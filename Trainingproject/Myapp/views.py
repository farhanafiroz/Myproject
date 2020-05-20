from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hey look! This is my first web page.")

def about(request):
    return HttpResponse(" This is about page.")

def contact(request):
    return HttpResponse("Please contact here.")

