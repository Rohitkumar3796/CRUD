from django import forms
from django.forms.forms import Form

from register.models import *
from django.forms import ModelForm

class empForm(ModelForm):

    class Meta:
       model = Employee
       fields = ['empId','empname','empemail','emppass','empmobile','empaddress']
       widgets = {
           'empId' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Employee ID'}),
           'empname' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
           'empemail' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
           'emppass' : forms.PasswordInput( render_value=True, attrs={'class':'form-control','placeholder':'Password'}),
           'empmobile' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone'}),
           'empaddress' : forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
       }
