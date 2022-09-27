import imp
import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from apps import room

import apps.room.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            apps.room.routing.websocket_urlpatterns
        )
    )
})
