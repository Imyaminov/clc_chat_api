from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from common.models import User
# Create your models here.


class Chat(models.Model):
    members = models.ManyToManyField(User)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.TextField()
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)


@receiver(post_save, sender=Message)
def my_handler(sender, instance, created, **kwargs):
    """
    Send message to channel
    """
    channel_layer = get_channel_layer()
    if created:

        # YANGI XABAR BO'LSA
        async_to_sync(channel_layer.group_send)(
            "clc", {"type": "chat_message", "data": {
                "id": instance.id,
                "status": "new_message",
                "text": instance.text,
                "chat_id": instance.chat_id,
                "from_user_id": instance.from_user_id,
            }}
        )
    else:
        # UPDATE BO'LSA
        async_to_sync(channel_layer.group_send)(
            "clc", {"type": "chat_message", "data": {
                "id": instance.id,
                "status": "updated_message",
                "text": instance.text,
                "chat_id": instance.chat_id,
                "from_user_id": instance.from_user_id,
            }}
        )
