from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from users.forms import CustomForm
from users.decorators import unauthorised_user
from Boomie.models import Category, Post, Comment, ReplyComment
from Boomie.filters import TitleFilter

def landing(request):
    post = Post.objects.all().order_by('-created_on')
    # search = TitleFilter(request.GET, queryset=post)
    # post = search.qs
    context = {
        'post': post,
        # 'search': search,
    }
    return render(request, 'users/landing_page.html')


#Helps us to authenticate this page.
#This page can only be accessed after user is logged in. 
@login_required(login_url = 'login') 
def dashboard(request):
    return render(request, 'users/dashboard.html')
    
@unauthorised_user
def register(request):
    form = CustomForm()

    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + ' ' + user)
            return redirect('login')
    
    context = {'form': form}
    return render(request, 'users/register.html', context)

@unauthorised_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password is incorrect')
    
    context = {}
    return render(request, 'registration/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')