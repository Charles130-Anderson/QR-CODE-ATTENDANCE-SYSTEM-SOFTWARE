#!/usr/bin/python3
"""URL configuration for FacultyView app."""
from . import views
from django.urls import path

urlpatterns = [
    # Path for the faculty view
    path("", views.faculty_view, name="faculty_view"),
    # Path for manual student addition
    path("add_manually", views.add_manually, name="add_manually"),
]
