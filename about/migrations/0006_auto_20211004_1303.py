# Generated by Django 3.1.3 on 2021-10-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_project_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='platforms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plat_name', models.CharField(max_length=100)),
                ('plat_icon', models.URLField(max_length=500)),
                ('plat_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='platforms',
            field=models.ManyToManyField(to='about.platforms'),
        ),
    ]