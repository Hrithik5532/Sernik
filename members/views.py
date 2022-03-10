
from urllib import request
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import SignUpForm
from django.contrib.auth.models import User
# Create your views here.
def UserRegistrationView(request):
    form_class = SignUpForm()
    if request.method =="POST":
        form = SignUpForm(request.POST)
        email = request.POST.get('email')

        if form.is_valid():
            if User.objects.filter(email__iexact=email).exists():
                messages.error(request,f"{email} is already used")
                return HttpResponseRedirect(reverse('register'))
            else:
                form.save()
                messages.success(request,"register")
                return render(request,"registration/login.html")
    return render(request,"registration/register.html",{'form':form_class})