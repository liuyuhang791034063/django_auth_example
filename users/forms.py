#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @Time     : 2018/3/8 21:06
__author__ = 'White'

from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
