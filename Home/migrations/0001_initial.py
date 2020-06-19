# Generated by Django 3.0.6 on 2020-06-14 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='images')),
                ('new_title', models.CharField(max_length=100)),
                ('map_snippet', models.CharField(max_length=500)),
                ('about', models.TextField()),
                ('history', models.TextField()),
                ('new', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/recent')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('icon', models.CharField(choices=[('fa fa-facebook', 'Facebook'), ('fa fa-twitter', 'Twitter'), ('fa fa-linkedin', 'LinkedIn'), ('fa fa-pintrest', 'Pintrest'), ('fa fa-snapchat', 'Snapchat'), ('fa fa-youtube', 'Youtube'), ('fa fa-reddit-alien', 'Reddit'), ('fa fa-medium', 'Medium'), ('fa fa-google-plus', 'Google Plus'), ('fa fa-js-fiddle', 'Fiddle'), ('fa fa-github', 'Github')], default='fa fa-facebook', max_length=120)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/services')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/slider')),
                ('name', models.CharField(max_length=20)),
                ('first', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.CharField(max_length=300)),
                ('video_content', models.TextField()),
            ],
        ),
    ]