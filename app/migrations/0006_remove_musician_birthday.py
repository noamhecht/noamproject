# Generated by Django 2.2.7 on 2020-01-29 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200129_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='birthday',
        ),
    ]
