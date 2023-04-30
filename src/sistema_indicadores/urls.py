"""URLs configuration module."""

# django
from django.urls import path, include

# Local
from sistema_indicadores import views

app_name = "kpi"
urlpatterns = [
    path("", views.index, name="index"),
    path("api/", include("sistema_indicadores.api.urls")),
]
