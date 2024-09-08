#!/usr/bin/python3
"""App configuration for FacultyView app."""
from django.apps import AppConfig


class FacultyviewConfig(AppConfig):
    """Configuration class for FacultyView app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FacultyView'
