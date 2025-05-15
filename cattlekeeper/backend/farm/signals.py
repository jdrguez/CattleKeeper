from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Animal

@receiver(post_save, sender=Animal)
def update_batch_quantity_on_animal_save(sender, instance, created, **kwargs):
    if created:  
        instance.batch.update_quantity()

@receiver(post_delete, sender=Animal)
def update_batch_quantity_on_animal_delete(sender, instance, **kwargs):
    instance.batch.update_quantity()