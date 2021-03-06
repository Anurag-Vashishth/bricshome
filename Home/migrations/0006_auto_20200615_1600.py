# Generated by Django 3.0.6 on 2020-06-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_about_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='reports/thumbnails')),
                ('image', models.ImageField(upload_to='reports/images')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('abstract', models.TextField()),
                ('complete', models.TextField()),
                ('pdf', models.FileField(upload_to='reports/file')),
            ],
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]
