# Generated by Django 2.1.3 on 2018-12-29 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('courses_contact', models.EmailField(blank=True, default='user@example.com', max_length=70, null=True, unique=True)),
                ('courses_image', models.ImageField(blank=True, upload_to='course_image')),
                ('city', models.CharField(default='Detroit', max_length=255)),
                ('location', location_field.models.plain.PlainLocationField(default='42.3314, -83.0458', max_length=63)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]