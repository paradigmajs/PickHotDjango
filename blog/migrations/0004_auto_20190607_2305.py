# Generated by Django 2.2.2 on 2019-06-07 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190607_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='static/img'),
        ),
    ]
