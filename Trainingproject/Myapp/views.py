from django.shortcuts import render
from django.http import HttpResponse
from.import forms
# Create your views here.

#def home(request):
#return HttpResponse("Hey look! This is my first web page.")
from .forms import Registerform


def home(request):
    return render(request,"Myapp/home.html")


def form_view(request):
    form = forms.Registerform
    if request.method == "POST":
        form = forms.Registerform(request.POST)
        if form.is_valid():
            print("validation worked")
            print("name: " + form.cleaned_data['first_name'])
            print("last_name: " + form.cleaned_data['last_name'])
            print("email: " + form.cleaned_data['email'])

    return render(request,"Myapp/index.html", {'form': form})
