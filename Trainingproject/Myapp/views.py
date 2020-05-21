from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#def home(request):
#return HttpResponse("Hey look! This is my first web page.")

def home(request):
    return render(request,"Myapp/home.html")

