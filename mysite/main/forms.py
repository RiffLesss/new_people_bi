from .models import Users, Orders
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['fuel', 'street', 'building']
        widgets = {
            "fuel": TextInput(attrs={
                "class": "form-control order-form-field order-fuel",
                "placeholder": "Топливо"
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


class RegisterForm(ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'surname', 'phone_number', 'email', 'password']
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control register-name",
                "placeholder": "Имя"
            }),
            "surname": TextInput(attrs={
                "class": "form-control register-surname",
                "placeholder": "Фамилия"
            }),
            "phone_number": TextInput(attrs={
                "class": "form-control register-phone",
                "placeholder": "Номер телефона"
            }),
            "email": EmailInput(attrs={
                "class": "form-control register-email",
                "placeholder": "Электронная почта"
            }),
            "password": PasswordInput(attrs={
                "class": "form-control register-password",
                "placeholder": "Пароль"
            })
        }


class LogInForm(ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'password']
        widgets = {
            "email": EmailInput(attrs={
                "class": "form-control login-email",
                "placeholder": "Электронная почта"
            }),
            "password": PasswordInput(attrs={
                "class": "form-control login-password",
                "placeholder": "Пароль"
            })
        }