# To make sure that your Celery app is loaded when you start Django, you should add it to "__all__:"

# from .celery import app as crypto_app

from __future__ import absolute_import, unicode_literals
from .celery import app as crypto_app
__all__ = ("crypto_app",)












