from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver 
from .models import Item
from core.logger import log_user_action


@receiver(post_save, sender = Item)
def log_item_save(sender, instance, created, **kwargs):
    
    if created: 
        log_user_action("CREATE_ITEM", instance.name)
    
    else: 
        log_user_action('UPDATE_ITEM', instance.name)
        
        
@receiver(post_delete, sender = Item)
def log_item_delete(sender, instance, **kwargs):
    log_user_action("DELETE_ITEM", instance.name)
