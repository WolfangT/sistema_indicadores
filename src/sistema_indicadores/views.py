"""Views for KPI module."""

# django]
from django.shortcuts import render


def index(request):
    """[TODO]."""
    return render(request, "sistema_indicadores/index.html", locals())
