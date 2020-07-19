"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    return render(request,'app/index.html')

def contact(request):
    """Renders the contact page."""
    return render(request,'app/contact.html')

def about(request):
    """Renders the about page."""
    return render(request,'app/about.html')
