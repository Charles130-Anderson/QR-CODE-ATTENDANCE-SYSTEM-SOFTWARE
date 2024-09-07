#!/usr/bin/python3
"""Migration for creating 'Student' model."""
from django.db import migrations, models


class Migration(migrations.Migration):
    """Handles migrations for the database."""

    initial = True  # Marks the initial migration

    dependencies = [
    ]  # Dependencies for this migration

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_roll', models.CharField(
                    max_length=20, primary_key=True, serialize=False
                )),
                ('s_name', models.CharField(max_length=50)),
                ('s_branch', models.CharField(max_length=10)),
                ('s_section', models.CharField(max_length=5)),
            ],
        ),
    ]  # Operations for creating models
