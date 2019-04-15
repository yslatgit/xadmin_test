# Generated by Django 2.2 on 2019-04-12 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='讲师姓名')),
                ('email', models.EmailField(max_length=30, verbose_name='讲师邮箱')),
                ('introduction', models.CharField(max_length=200, verbose_name='讲师简介')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '讲师信息',
                'verbose_name_plural': '讲师信息',
            },
        ),
        migrations.CreateModel(
            name='VideoSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='视频名称')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '视频信息',
                'verbose_name_plural': '视频信息',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='章节名称')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.VideoSource', verbose_name='视频名称')),
            ],
            options={
                'verbose_name': '章节信息',
                'verbose_name_plural': '章节信息',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='课程名称')),
                ('time', models.CharField(max_length=100, verbose_name='课程时长（小时）')),
                ('type', models.CharField(choices=[(0, 'JAVA'), (1, 'PYTHON'), (2, 'C'), (3, 'C++')], default=1, max_length=10, verbose_name='课程类型')),
                ('level', models.CharField(choices=[(0, '初级'), (1, '中级'), (2, '高级')], default=0, max_length=2, verbose_name='课程等级')),
                ('introduction', models.CharField(max_length=200, verbose_name='课程简介')),
                ('studey_num', models.CharField(max_length=2000, verbose_name='学习人数')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.Section', verbose_name='章节名称')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.Teacher', verbose_name='讲师姓名')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
            },
        ),
    ]