# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import re_path
from .consumers import VideoConsumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                re_path(r'ws/video/(?P<video_id>\d+)/$', VideoConsumer.as_asgi()),
            ]
        )
    ),
})
