# Generated by Django 2.1.3 on 2019-01-03 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_auto_20190101_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]