# asgi.py

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path
from crypto import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feenax.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/crypto/", consumers.CryptoConsumer.as_asgi()),
        ])
    ),
})