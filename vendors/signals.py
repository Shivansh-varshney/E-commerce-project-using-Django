from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vendor
from django.contrib.auth.models import Group


@receiver(post_save, sender=Vendor)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        add_group = Group.objects.get(name='vendor')
        remove_group = Group.objects.get(name='customer')
        instance.user.groups.add(add_group)
        instance.user.groups.remove(remove_group)
