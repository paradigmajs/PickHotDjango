# Generated by Django 2.2.2 on 2019-06-11 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190611_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guests',
            old_name='author',
            new_name='authorgusts',
        ),
        migrations.RenameField(
            model_name='hot',
            old_name='author',
            new_name='authorhot',
        ),
    ]
