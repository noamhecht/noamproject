# Generated by Django 2.2.7 on 2020-03-31 10:11

import app.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='musician_pics')),
                ('instrument', models.IntegerField(blank=True, choices=[(1, 'GUITAR'), (2, 'DRUMS'), (3, 'BASS'), (4, 'KEYBOARDS')], default=app.utils.InstrumentTypes(1), null=True)),
                ('playing_level', models.IntegerField(blank=True, choices=[(1, 'MASTER'), (2, 'HIGH'), (3, 'MEDIUM'), (4, 'LOW')], default=app.utils.PlayingLevelTypes(4), null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
