from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/auth_form.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/auth_form.html', context)

@ login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')