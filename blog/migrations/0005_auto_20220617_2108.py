# Generated by Django 3.2 on 2022-06-17 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220617_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publish_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='update_date',
        ),
    ]
