from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Owner_model


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Owner_model.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.owner_model.save()