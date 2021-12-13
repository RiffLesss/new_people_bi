from django.shortcuts import render, redirect
from .forms import OrderForm, RegisterForm, LogInForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Orders


def index(request):
    return render(request, 'main/main-page.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            print(form.errors)
    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'main/register-page.html', context)


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user, username, password)
        if user is not None:
            login(request, user)
            print(user.is_authenticated)
            return redirect('/')
    form = LogInForm()
    context = {
        'form': form
    }
    return render(request, 'main/login-page.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        form.user_id = 1
        if form.is_valid():
            form.save()
            return redirect('/order/complete')
        else:
            print('Что-то пошло не так')
    form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'main/order-page.html', context)


@login_required(login_url='/login')
def order_complete(request):
    return render(request, 'main/order-complete.html')