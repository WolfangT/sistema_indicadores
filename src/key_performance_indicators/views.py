"""Views for KPI module."""

# django]
from django.shortcuts import render


def index(request):
    """[TODO]."""
    return render(request, "key_performance_indicators/index.html", locals())
