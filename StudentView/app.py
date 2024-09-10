#!/usr/bin/python3
from django.apps import AppConfig
"""Configuration module"""


class StudentviewConfig(AppConfig):
    """
    Configuration for the StudentView app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'StudentView'
