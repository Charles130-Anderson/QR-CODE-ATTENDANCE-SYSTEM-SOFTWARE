#!/usr/bin/python3
"""Model definitions for FacultyView app."""
from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)


class Section(models.Model):
    """Model representing a section."""
    section = models.CharField(max_length=2)

    def __str__(self) -> str:
        """Return section as string."""
        return self.section


class Year(models.Model):
    """Model representing a year."""
    year = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)],
    )

    def __str__(self) -> str:
        """Return year as string."""
        return str(self.year)


class Branch(models.Model):
    """Model representing a branch."""
    branch = models.CharField(max_length=10)

    def __str__(self) -> str:
        """Return branch as string."""
        return self.branch


class Student(models.Model):
    """Model representing a student."""
    s_roll = models.CharField(max_length=20, primary_key=True)
    s_fname = models.CharField(max_length=20)
    s_lname = models.CharField(max_length=20)
    s_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    s_section = models.ForeignKey(Section, on_delete=models.CASCADE)
    s_year = models.ForeignKey(Year, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Return student details string."""
        return (
            f"{self.s_fname} {self.s_lname} - "
            f"{self.s_roll} - {self.s_branch}"
            f"({self.s_year}{self.s_section})"
        )
