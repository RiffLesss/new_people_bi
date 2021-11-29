from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Users(models.Model):
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField('Почта', max_length=50, primary_key=True)
    password = models.CharField('Пароль', max_length=150)


class Orders(models.Model):
    fuel = models.CharField('Топливо', max_length=30)
    street = models.CharField('Улица', max_length=30)
    building = models.CharField('Здание', max_length=30)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)



