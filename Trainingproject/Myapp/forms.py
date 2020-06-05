from django import forms
from django.core import validators
from .models import Register
from django.forms import ModelForm

#def check(value):
    #if value[0].lower()!='a':
    #raise forms.ValidationError("Please start a name with a")

#def valid(password):
    #if len(password) < 6:
        #raise forms.ValidationError("Please enter more than 6 characters")


class Registration(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    verify_password = forms.CharField(widget=forms.PasswordInput,label="Re-enter the Password")

class Registerform(forms.ModelForm):
    class Meta:
        model=Register
        fields="__all__"

def clean(self):
    super(Registration,self).clean()

    password = self.cleaned_data.get('password')
    UpperPass = 0
    LowerPass = 0
    dititPass = 0
    spChar = ''
    UpperPass = sum(1 for i in password if i.isupper())
    LowerPass = sum(1 for i in password if i.isupper())
    dititPass = sum(1 for i in password if i.isdigit())
    spChar = re.sub('[\w]+', '', password)

    if ((UpperPass < 1) or (LowerPass < 1) or (dititPass < 1) or (len(spChar) < 1)):
        self._errors['password'] = self.error_class(["Password needs to have at-least 1 lower case letter, 1 upper case letter, 1 digit, and 1 special character"])

    verify_password = self.cleaned_data.get('verify_password')

    if password != verify_password:
        self._errors['verify_password'] = self.error_class(["Password Doesn't Match"])

#class Registerform(forms.Form):
    #first_name=forms.CharField(label="Enter your first name")
    #last_name = forms.CharField(label="Enter your last name")
    #email= forms.EmailField(max_length=30)
    #verify_email= forms.EmailField(label="Repeat E-mail")
    #comment= forms.CharField(widget=forms.Textarea)
    #password= forms.CharField(widget=forms.PasswordInput, validators=[valid])

#def clean(self):
    #email = self.cleaned_data['email']
    #vemail = self.cleaned_data['verify_email']
    #if email!=vemail:
        #raise forms.ValidationError("Email doesn't match")
