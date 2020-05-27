from django import forms

class Registerform(forms.Form):
    first_name=forms.CharField(label="Enter your first name")
    last_name = forms.CharField(label="Enter your last name")
    email= forms.EmailField(max_length=30)
    comment= forms.CharField(widget=forms.Textarea)
