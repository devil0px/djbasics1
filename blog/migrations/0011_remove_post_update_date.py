# Generated by Django 3.2 on 2022-06-18 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_update_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='update_date',
        ),
    ]