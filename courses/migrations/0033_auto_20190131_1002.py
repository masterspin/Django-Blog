# Generated by Django 2.1.3 on 2019-01-31 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0032_auto_20190102_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='price',
        ),
        migrations.RemoveField(
            model_name='post',
            name='schedule',
        ),
    ]
