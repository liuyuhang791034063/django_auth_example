#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @Time     : 2018/3/9 21:52
__author__ = 'White'

from .models import User

class EmailBackend(object):
    def authenticate(self, request, **credentials):
        email = credentials.get('email', credentials.get('username'))
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            pass
        else:
            if user.check_password(credentials["password"]):
                return user

    def get_user(self, use_id):
        try:
            return User.objects.get(pk = use_id)
        except User.DoseNotExist:
            return None