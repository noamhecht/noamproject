from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from .utils import InstrumentTypes, PlayingLevelTypes


class Musician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='musician_pics')
    instrument = models.IntegerField(choices=InstrumentTypes.choices(), default=InstrumentTypes.GUITAR,
                                     blank=True, null=True)
    playing_level = models.IntegerField(choices=PlayingLevelTypes.choices(), default=PlayingLevelTypes.LOW,
                                        blank=True, null=True)
    # first_name = models.CharField(max_length=20, blank=True, null=True)
    # last_name = models.CharField(max_length=20, blank=True, null=True)
    # ('^(05)[0-4][0-9]{7}$')
    # birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Musician'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)




