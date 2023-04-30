"""KPI API tests module."""

# django
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .factories import OrganizationFactory


class OrganizationAPITests(APITestCase):
    """Tests for the Organization API."""

    def test_get_organization_list(self):
        for i in range(100):
            OrganizationFactory()

        response = self.client.get("/kpi/api/organization/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 100)
