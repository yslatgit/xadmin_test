#coding:utf-8
from django.db import models

from users.models import UserProfile
# Create your models here.
class VideoSource(models.Model):
    name = models.CharField(max_length=30,verbose_name='视频名称')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '视频信息'
        verbose_name_plural = verbose_name


class Section(models.Model):
    name = models.CharField(max_length=30,verbose_name='章节名称')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    video= models.ForeignKey(VideoSource,null=True,blank=True,on_delete=models.SET_NULL,verbose_name='视频名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '章节信息'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    name = models.CharField(max_length=10,verbose_name='讲师姓名')
    email = models.EmailField(max_length=30,verbose_name='讲师邮箱')
    introduction = models.CharField(max_length=200, verbose_name='讲师简介')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '讲师信息'
        verbose_name_plural = verbose_name


class Course(models.Model):
    name = models.CharField(max_length=20,verbose_name='课程名称')
    time = models.CharField(max_length=100,verbose_name='课程时长（小时）')
    CHOICES=((0,'JAVA'),(1,'PYTHON'),(2,'C'),(3,'C++'))
    type = models.IntegerField(choices=CHOICES,default=1,verbose_name='课程类型')
    level = models.IntegerField(choices=((0,'初级'),(1,'中级'),(2,'高级')),default=0,verbose_name='课程等级')
    introduction = models.CharField(max_length=200,verbose_name='课程简介')
    studey_num = models.CharField(max_length=2000,verbose_name='学习人数')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    section = models.ForeignKey(Section,null=True,blank=True,on_delete=models.SET_NULL,verbose_name='章节名称')
    teacher= models.ForeignKey(Teacher,null=True,blank=True,on_delete=models.SET_NULL,verbose_name='讲师姓名')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name







