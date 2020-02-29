from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import birthday
from enum import Enum
import uuid
from .utils import InstrumentTypes, PlayingLevelTypes


class Musician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='musician_pics')
    email_confirmed = models.BooleanField(default=False)
    instrument = models.IntegerField(choices=InstrumentTypes.choices(), default=InstrumentTypes.GUITAR)
    playing_level = models.IntegerField(choices=PlayingLevelTypes.choices(), default=PlayingLevelTypes.LOW)

    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    # city = models.CharField(max_length=200)
    # email = models.EmailField
    # phone_number = models.IntegerField()
    # birthday = birthday.fields.BirthdayField()
    # unique_id = uuid.uuid4().hex

    def __str__(self):
        return f'{self.user.username} Musician'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)




