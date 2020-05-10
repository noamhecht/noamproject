from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from .utils import InstrumentTypes, PlayingLevelTypes
from cities_light.models import City, Region
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import datetime


class Musician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='musician_pics')
    instrument = models.IntegerField(choices=InstrumentTypes.choices(), default=InstrumentTypes.GUITAR,
                                     blank=True, null=True)
    playing_level = models.IntegerField(choices=PlayingLevelTypes.choices(), default=PlayingLevelTypes.LOW,
                                        blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^(05)[0-4][0-9]{7}$',
                                 message="Please enter a valid phone number")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    birthday = models.DateField(blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    # region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    # def clean(self, *args, **kwargs):
    #     super(Musician, self).clean(*args, **kwargs)
    #
    #     if self.birthday > datetime.date.today():
    #         raise ValidationError('Birthday can't be in the future')

