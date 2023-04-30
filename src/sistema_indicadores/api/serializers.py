from rest_framework import serializers

from sistema_indicadores.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ("name",)
