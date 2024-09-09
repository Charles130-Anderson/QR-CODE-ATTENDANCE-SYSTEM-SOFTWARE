#!/usr/bin/python3
"""
Django views for handling student
submissions and displaying confirmation.
"""

from django.shortcuts import render
from FacultyView.models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

present = set()


def add_manually_post(request):
    """
    Add student to the set.
    Retrieves student by roll number.
    """
    student_roll = request.POST["student-name"]
    student = Student.objects.get(s_roll=student_roll)
    present.add(student)
    return HttpResponseRedirect("/submitted")


def submitted(request):
    """
    Render the submitted page.
    Displays confirmation page to user.
    """
    return render(request, "StudentView/Submitted.html")
