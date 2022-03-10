from ast import arg
from statistics import mode
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','style':'border-style: outset;'}))
    first_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','style':'border-style: outset;'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','style':'border-style: outset;'}))

    class Meta:

        model=User
        fields=['username','first_name','last_name','email','password1','password2']
    def __init__(self,*args, **kwargs):
            super(SignUpForm,self).__init__(*args,**kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['style'] ='border-style: outset;'
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['style'] ='border-style: outset;'
            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['style'] ='border-style: outset;'


    # def clean_email(self):
    #     # Get the email
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email__iexact=email).exists():
    #         raise forms.ValidationError("User with that email already exists")
    #     return email