#!/usr/bin/python3
"""
Django project management script.

Sets up environment and executes commands.
"""

import os
import sys


def main():
    """
    Set up Django environment and
    execute command line management.
    """
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE', 'QR_Attendance_System.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
