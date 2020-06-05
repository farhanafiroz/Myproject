from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from .forms import Registerform
# Create your views here.

#def home(request):
     #return HttpResponse("Hey look! This is my first web page.")

def home(request):
    return render(request, "Myapp/home.html")


# def form_view(request):
# form = forms.Registerform
# if request.method == "POST":
# form = forms.Registerform(request.POST)
# if form.is_valid():
# print("validation worked")
# print("name: " + form.cleaned_data['first_name'])
# print("last_name: " + form.cleaned_data['last_name'])
# print("email: " + form.cleaned_data['email'])

# return render(request,"Myapp/index.html", {'form': form})


def create(request):
    if request.method == 'POST':
        form = forms.Registerform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("success")
            except:
                print("Error saving form")
    else:
        form = forms.Registerform()
        return render(request, 'Myapp/index.html', {'form': form})


def success(request):
    return render(request, 'Myapp/success.html')