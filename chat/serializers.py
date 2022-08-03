from rest_framework import serializers
from chat.models import Chat, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class ChatListSerializer(serializers.ModelSerializer):
    last_message_date = serializers.DateTimeField()
    last_message = serializers.StringRelatedField()
    profile_image = serializers.StringRelatedField()
    profile_title = serializers.StringRelatedField()
    is_unmuted = serializers.BooleanField()

    class Meta:
        model = Chat
        fields = ('id', 'last_message', 'last_message_date',
                  "profile_image", 'profile_title','is_unmuted')
