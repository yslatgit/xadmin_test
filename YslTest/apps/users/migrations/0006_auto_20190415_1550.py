# Generated by Django 2.2 on 2019-04-15 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190415_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverfiy',
            name='type',
            field=models.IntegerField(choices=[(0, '注册'), (1, '忘记密码')], default=0, verbose_name='邮件类型'),
        ),
    ]