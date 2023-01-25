# Generated by Django 4.0.1 on 2022-02-20 03:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_auto_20211015_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='about',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
