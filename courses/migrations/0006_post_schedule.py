# Generated by Django 2.1.3 on 2018-12-29 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_post_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='schedule',
            field=models.TextField(default='Monday: 5:30-6:30\n\t\tTuesday: 6:30-7:30'),
        ),
    ]
