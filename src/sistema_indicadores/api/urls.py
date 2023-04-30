from django.urls import include, path

from rest_framework import routers

from sistema_indicadores.api.views import OrganizationViewSet

router = routers.DefaultRouter()
router.register(r"organization", OrganizationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
