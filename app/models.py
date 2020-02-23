from django.db import models
from django.contrib.auth.models import User
import birthday
from enum import Enum
import uuid
from .utils import InstrumentTypes, PlayingLevelTypes


class Musician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='musician_pics')
    email_confirmed = models.BooleanField(default=False)

    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    # city = models.CharField(max_length=200)
    # email = models.EmailField
    # phone_number = models.IntegerField()
    # birthday = birthday.fields.BirthdayField()
    # instrument = models.IntegerField(choices=InstrumentTypes.choices(), default=InstrumentTypes.GUITAR)
    # playing_level = models.IntegerField(choices=PlayingLevelTypes.choices(), default=PlayingLevelTypes.HIGH)
    # unique_id = uuid.uuid4().hex

    def __str__(self):
        return f'{self.user.username} Musician'





