# Generated by Django 4.0.5 on 2022-06-14 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_twitter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
