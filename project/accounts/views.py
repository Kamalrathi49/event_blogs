from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, f'Welcome to Web Board {request.user}!')
            return redirect('/')
        else :
            messages.error(request, f'something went wrong')
            return redirect('/accounts/signup')
    else:
        form = RegisterForm()
        ctx = {'form' : form}
        return render(request, 'accounts/signup.html', ctx)


def log_out(request):
    logout(request)
    messages.success(request,'You have logged out sucessfully!')
    return redirect('/')



def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
                messages.success(request,f'welcome back {username}')
                return redirect('/')
            else:
                messages.error(request,f"username and password does not match! please try again")
                return redirect('/accounts/login')


        else :
            messages.error(request, f'something went wrong')
            return redirect('accounts/login')
    else:
        form = LoginForm()
        ctx = {'form' : form}
        return render(request, 'accounts/login.html', ctx)
    
