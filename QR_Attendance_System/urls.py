#!/usr/bin/python3
"""
URL configuration for QR_Attendance_System.

Defines URL routing for project.
"""

from django.contrib import admin
from django.urls import path, include

# URL patterns for routing views.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("FacultyView.urls")),
    path("", include("StudentView.urls")),
]
