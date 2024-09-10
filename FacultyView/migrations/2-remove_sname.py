#!/usr/bin/python3
"""Migration for modifying 'Student' model."""
from django.db import migrations, models


class Migration(migrations.Migration):
    """Handles database migration changes."""

    dependencies = [
        ('FacultyView', '1-initial'),
    ]  # Dependencies for this migration

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='s_name',
        ),  # Remove 's_name' field from 'Student'

        migrations.AddField(
            model_name='student',
            name='s_fname',
            field=models.CharField(default=5, max_length=20),
            preserve_default=False,
        ),  # Add 's_fname' field to 'Student'

        migrations.AddField(
            model_name='student',
            name='s_lname',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),  # Add 's_lname' field to 'Student'
    ]  # Operations to modify models
