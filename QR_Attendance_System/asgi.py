#!/usr/bin/python3

"""
ASGI config for QR_Attendance_System project.

It exposes the ASGI callable as
a module-level variable named `application`.

For more information on this file,
see https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Set default settings module environment
os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE', 'QR_Attendance_System.settings'
        )

# Get the ASGI application callable
application = get_asgi_application()
