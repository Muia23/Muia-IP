# Generated by Django 3.1.3 on 2021-09-16 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectimages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageurl', models.URLField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image',
        ),
        migrations.AddField(
            model_name='project',
            name='project_images',
            field=models.ManyToManyField(to='about.projectimages'),
        ),
    ]