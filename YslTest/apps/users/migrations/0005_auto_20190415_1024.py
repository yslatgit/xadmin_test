# Generated by Django 2.2 on 2019-04-15 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190415_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverfiy',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='邮箱地址'),
        ),
    ]
