from .models import Users, Orders
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['fuel', 'amount', 'street', 'building']
        widgets = {
            "fuel": TextInput(attrs={
                "class": "form-control order-form-field order-fuel",
                "placeholder": "Топливо"
            }),
            "amount": TextInput(attrs={
                "class": "form-control order-form-field order-amount",
                "placeholder": "Объём в литрах"
            }),
            "street": TextInput(attrs={
                "class": "form-control order-form-field order-street",
                "placeholder": "Улица"
            }),
            "building": TextInput(attrs={
                "class": "form-control order-form-field order-building",
                "placeholder": "Дом"
            })
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            "username": TextInput(attrs={
                "class": "form-control register-name",
                "placeholder": "Имя пользователя"
            }),
            "first_name": TextInput(attrs={
                "class": "form-control register-first-name",
                "placeholder": "Имя"
            }),
            "last_name": TextInput(attrs={
                "class": "form-control register-last-name",
                "placeholder": "Фамилия"
            }),
            "email": EmailInput(attrs={
                "class": "form-control register-email",
                "placeholder": "Электронная почта"
            }),
            "password1": PasswordInput(attrs={
                "class": "form-control register-password",
                "placeholder": "Пароль"
            }),
            "password2": PasswordInput(attrs={
                "class": "form-control register-password-repeat",
                "placeholder": "Повторите пароль"
            })
        }


class LogInForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            "username": TextInput(attrs={
                "class": "form-control login-username",
                "placeholder": "Имя пользователя"
            }),
            "password": PasswordInput(attrs={
                "class": "form-control login-password",
                "placeholder": "Пароль"
            })
        }