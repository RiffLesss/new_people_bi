from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('order', views.order),
    path('register', views.register),
    path('login', views.loginUser),
    path('logout', views.logoutUser),
    path('order/complete', views.order_complete)
]