#coding:utf-8
from django.db import models
from users.models import UserProfile
from course.models import Course

# Create your models here.
class MyComments(models.Model):
    user_name = models.ForeignKey(UserProfile,null=True,blank=True,on_delete=models.SET_NULL,verbose_name='用户姓名')
    course_name = models.ForeignKey(Course,null=True,blank=True,on_delete=models.SET_NULL,verbose_name='课程名称')
    comments = models.TextField(verbose_name='评论内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.user_name.username
        # return '%s'%self.id

    class Meta:
        verbose_name = '评论信息'
        verbose_name_plural = verbose_name