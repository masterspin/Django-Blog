# Generated by Django 2.1.3 on 2019-01-03 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0030_auto_20190102_2044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='mainImage',
            new_name='main_Image',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='subImage1',
            new_name='sub_Image1',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='subImage2',
            new_name='sub_Image2',
        ),
    ]
