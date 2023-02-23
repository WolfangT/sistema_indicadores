"""URLs configuration module."""

# django
from django.urls import path

# Local
from key_performance_indicators import views

app_name = "kpi"
urlpatterns = [
    path("", views.index, name="index"),
]
