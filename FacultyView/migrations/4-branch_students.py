#!/usr/bin/python3
"""Migration for creating new models."""
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Handles database migration changes."""

    dependencies = [
        ('FacultyView', '3-student_s_year.py'),
    ]  # Dependencies for this migration

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID'
                )),
                ('branch', models.CharField(max_length=10)),
            ],
        ),  # Create 'Branch' model

        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID'
                )),
                ('section', models.CharField(max_length=2)),
            ],
        ),  # Create 'Section' model

        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID'
                )),
                ('year', models.IntegerField(
                    validators=[
                        django.core.validators.MinValueValidator(1),
                        django.core.validators.MaxValueValidator(4)
                    ]
                )),
            ],
        ),  # Create 'Year' model

        migrations.AlterField(
            model_name='student',
            name='s_branch',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='FacultyView.branch'
            ),
        ),  # Alter 's_branch' to foreign key

        migrations.AlterField(
            model_name='student',
            name='s_section',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='FacultyView.section'
            ),
        ),  # Alter 's_section' to foreign key

        migrations.AlterField(
            model_name='student',
            name='s_year',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='FacultyView.year'
            ),
        ),  # Alter 's_year' to foreign key
    ]  # Operations to modify models
