from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Users(models.Model):
    id = models.AutoField(auto_created=True, unique=True, primary_key=True)
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField('Почта', max_length=50)
    password = models.CharField('Пароль', max_length=150)


class Orders(models.Model):
    #id = models.AutoField(auto_created=True, unique=True)
    fuel = models.CharField('Топливо', max_length=30)
    street = models.CharField('Улица', max_length=30)
    amount = models.CharField('Объём', max_length=30)
    building = models.CharField('Здание', max_length=30)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
