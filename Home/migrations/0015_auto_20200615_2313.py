# Generated by Django 3.0.6 on 2020-06-15 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_auto_20200615_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='map_snippet',
            new_name='venue',
        ),
    ]
