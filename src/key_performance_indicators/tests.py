"""KPI tests module."""

# django
from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):
    """Tests for the index page."""

    def test_responce_ok(self):
        """Checks that the page responds for requests."""
        response = self.client.get(reverse("kpi:index"))
        self.assertEqual(response.status_code, 200)
