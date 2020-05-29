from django import forms
from django.core import validators

#def check(value):
    #if value[0].lower()!='a':
    #raise forms.ValidationError("Please start a name with a")

def valid(password):
    if len(password) < 6:
        raise forms.ValidationError("Please enter more than 6 characters")


class Registerform(forms.Form):
    first_name=forms.CharField(label="Enter your first name")
    last_name = forms.CharField(label="Enter your last name")
    email= forms.EmailField(max_length=30)
    verify_email= forms.EmailField(label="Repeat E-mail")
    comment= forms.CharField(widget=forms.Textarea)
    password= forms.CharField(widget=forms.PasswordInput, validators=[valid])

