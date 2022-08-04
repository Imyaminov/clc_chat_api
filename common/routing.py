from django.urls import re_path

from . import consumer

websocket_urlpatterns = [
    re_path('ws/<str:chat_id>', consumer.ChatConsumer.as_asgi()),
    re_path('ws/', consumer.ChatConsumer.as_asgi()),

]
