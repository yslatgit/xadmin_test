#coding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserProfile(AbstractUser):
    # username = models.CharField(max_length=20,verbose_name='用户名')
    # password = models.CharField(max_length=30,verbose_name='密码')
    # email = models.EmailField(max_length=20,null=True,blank=True,verbose_name='邮箱地址')
    CHOICES = ((1,'超级管理员'),(2,'管理员'),(3,'普通用户'),(4,'游客'))
    type = models.CharField(max_length=6,choices=CHOICES,default=3,verbose_name='用户类型')
    head_img = models.ImageField(upload_to='head_img/%Y/%m/%d',verbose_name='用户头像')
    gender = models.CharField(max_length=6,default='male',choices=(('male','男'),('female','女')),verbose_name='性别')
    learn_time = models.CharField(max_length=1000,verbose_name='学习时长（小时）')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

class EmailVerfiy(models.Model):
    email = models.EmailField(max_length=50,verbose_name='邮箱地址')
    type = models.IntegerField(choices=((0,'注册'),(1,'忘记密码')),default=0,verbose_name='邮件类型')
    send_time = models.DateTimeField(auto_now=True,verbose_name='发送时间')

    class Meta:
        verbose_name ='邮箱验证'
        verbose_name_plural = verbose_name


