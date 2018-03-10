#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @Time     : 2018/3/8 21:20
__author__ = 'White'

from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name= 'register'),
]