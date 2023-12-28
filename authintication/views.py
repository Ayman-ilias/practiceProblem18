from django.shortcuts import render, redirect
from .import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import time
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Registered successfully')
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form': register_form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password = user_pass)
            if user is not None:
                login(request, user)
                messages.success(request,'Logged In Successfully')
                return redirect('home')
            else:
                messages.success(request,'Information does not match')
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request,'user_login.html',{'form' : form})

def user_logout(request):
    logout(request)
    messages.info(request,"Logged out successfully")
    return redirect('user_login')