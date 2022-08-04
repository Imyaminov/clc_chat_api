from django.urls import path
from chat import views
urlpatterns = [
    path("chat/", views.ChatListView.as_view(), name='chat'),
    path('message/<int:chat>', views.MessageApiView.as_view(), name='chat_message')
]