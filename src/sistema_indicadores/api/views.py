from rest_framework import viewsets

from sistema_indicadores.api.serializers import OrganizationSerializer
from sistema_indicadores.models import Organization


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
