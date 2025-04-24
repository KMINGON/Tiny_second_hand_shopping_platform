from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/1to1/(?P<room_name>[\w_]+)/$', consumers.OneToOneChatConsumer.as_asgi()),
]
