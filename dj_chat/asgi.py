# mysite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_chat.settings")

# django channels making use of and checking the protocol type before routing
application = ProtocolTypeRouter({
  "http": get_asgi_application() ,  #findout if i need to change this http to httpson production
  "websocket": AuthMiddlewareStack (
        URLRouter (
            chat.routing.websocket_urlpatterns
        )
    ),
})