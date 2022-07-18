from django.contrib import admin
from django.urls import path, include
from authenication_user.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('register', register, name="register"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
]
