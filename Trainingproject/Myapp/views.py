from django.shortcuts import render
from django.http import HttpResponse
from.import forms
# Create your views here.

#def home(request):
#return HttpResponse("Hey look! This is my first web page.")

def home(request):
    return render(request,"Myapp/home.html")

def form_view(request):
    if request.method:
        form=forms.Registerform
    return render(request,"Myapp/index.html", {'form':form})