# Generated by Django 2.2.7 on 2020-03-17 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200229_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='email_confirmed',
        ),
    ]