from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, SignInForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('posts_list_url')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('posts_list_url')


def login_view(request):
    if request.method == 'POST':
        form = SignInForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print("username",  username)
            print("password",  password)
            user = authenticate(username=username, password=password)
            if user is not None:
                print("user", user)
                print("request", request)
                login(request, user)
                return redirect('posts_list_url')
            else:
                print('User not found')
    else:
        form = SignInForm()
    return render(request, 'users/login.html', {'form': form})
