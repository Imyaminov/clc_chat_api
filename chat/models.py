from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from common.models import User
# Create your models here.


class Chat(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to="chat/", null=True, blank=True)

    members = models.ManyToManyField(User, related_name="chat")
    pinned = models.ManyToManyField(User, related_name='user_pinned')
    unmuted = models.ManyToManyField(User, related_name='user_unmuted')
    is_group = models.BooleanField(default=False)
    is_archived = models.ManyToManyField(User, related_name='user_archived')


class Message(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField()
    image = models.ImageField(upload_to='image_image', blank=True)
    icon = models.FileField(upload_to='message_icons/', blank=True)
    read = models.ManyToManyField(User, related_name='user_read', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Message)
def my_handler(sender, instance, created, **kwargs):
    """
    Send message to channel
    """
    channel_layer = get_channel_layer()
    if created:
        # YANGI XABAR BO'LSA
        async_to_sync(channel_layer.send)(
            "clc", {"type": "chat_message", "data": {
                # 'user': user.username,
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

# @receiver(post_save, sender=User)
# def my_handler(sender, instance, created, **kwargs):
#     """
#     Send message to channel
#     """
#     channel_layer = get_channel_layer()
#
#     if instance.is_online:
#
#         async_to_sync(channel_layer.group_send)(
#             "clc", {"type": "chat_message", "data": {
#                 "id": instance.id,
#                 "status": "online",
#                 "email": instance.email,
#             }}
#         )
#     else:
#         async_to_sync(channel_layer.group_send)(
#             "clc", {"type": "chat_message", "data": {
#                 "id": instance.id,
#                 "status": "offline",
#                 "email": instance.email,
#             }}
#         )
