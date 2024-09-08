#!/usr/bin/python3
"""URL configuration for FacultyView app."""
from . import views
from django.urls import path

urlpatterns = [
    path("", views.faculty_view, name="faculty_view"),
    """Path for the faculty view."""
    path("add_manually", views.add_manually, name="add_manually"),
    """Path for manual student addition."""
]
