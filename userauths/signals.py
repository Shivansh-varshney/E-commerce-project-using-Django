from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from userauths.models import User


@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        customer_group, _ = Group.objects.get_or_create(name='customer')
        instance.groups.add(customer_group)