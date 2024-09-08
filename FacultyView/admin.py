#!/usr/bin/python3
"""Admin registration for models."""
from django.contrib import admin
# Register your models here.

from .models import Student, Section, Year, Branch

admin.site.register(Student)  # Register Student model
admin.site.register(Section)  # Register Section model
admin.site.register(Year)     # Register Year model
admin.site.register(Branch)   # Register Branch model
