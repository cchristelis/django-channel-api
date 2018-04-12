import core
import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.prod_docker")
channel_layer = channels.asgi.get_channel_layer()