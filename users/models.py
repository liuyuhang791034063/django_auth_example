from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True) #blank = True 注册时不需要填写昵称

    class Meta(AbstractUser.Meta):
        pass

class Profile(models.Model):
    nickname = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
