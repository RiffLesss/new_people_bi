from django.shortcuts import render, redirect
from .forms import OrderForm, RegisterForm, LogInForm


def index(request):
    return render(request, 'main/main-page.html')


def order(request):
    form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'main/order-page.html', context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            print('Что-то пошло не так')
    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'main/register-page.html', context)


def login(request):
    form = LogInForm()
    context = {
        'form': form
    }
    return render(request, 'main/login-page.html', context)


def order_complete(request):
    return render(request, 'main/order_complete.html')