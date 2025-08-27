from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Property


@receiver(post_delete, sender=Property, dispatch_uid='property_deleted')
def property_delete_handler(sender, **kwargs):
    cache.delete('all_properties')


@receiver(post_save, sender=Property, dispatch_uid='property_updated')
def property_update_handler(sender, **kwargs):
    cache.delete('all_properties')
