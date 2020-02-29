# Generated by Django 2.2.7 on 2020-02-29 20:52

import app.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_musician_email_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='instrument',
            field=models.IntegerField(choices=[(1, 'GUITAR'), (2, 'DRUMS'), (3, 'BASS'), (4, 'KEYBOARDS')], default=app.utils.InstrumentTypes(1)),
        ),
        migrations.AddField(
            model_name='musician',
            name='playing_level',
            field=models.IntegerField(choices=[(1, 'MASTER'), (2, 'HIGH'), (3, 'MEDIUM'), (4, 'LOW')], default=app.utils.PlayingLevelTypes(2)),
        ),
    ]
