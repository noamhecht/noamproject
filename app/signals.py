from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Musician


# @receiver(post_save, sender=User)
# def create_musician(sender, instance, created, **kwargs):
#     if created:
#         Musician.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_musician(sender, instance, **kwargs):
#     instance.musician.save()
