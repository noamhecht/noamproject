# Generated by Django 2.2.7 on 2020-02-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200208_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
