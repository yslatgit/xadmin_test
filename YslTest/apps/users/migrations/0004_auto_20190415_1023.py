# Generated by Django 2.2 on 2019-04-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190415_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverfiy',
            name='type',
            field=models.IntegerField(choices=[(0, '注册'), (1, '忘记密码')], default=0, max_length=10, verbose_name='邮件类型'),
        ),
    ]