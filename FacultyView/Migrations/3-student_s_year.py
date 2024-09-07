#!/usr/bin/python3
"""Migration for modifying 'Student' model."""
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    """Handles database migration changes."""

    dependencies = [
        ('FacultyView', '0002_remove_student_s_name_student_s_fname_and_more'),
    ]  # Dependencies for this migration

    operations = [
        migrations.AddField(
            model_name='student',
            name='s_year',
            field=models.IntegerField(
                default=1,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(4)
                ]
            ),
            preserve_default=False,
        ),  # Add 's_year' field to 'Student'
    ]  # Operations to modify models
