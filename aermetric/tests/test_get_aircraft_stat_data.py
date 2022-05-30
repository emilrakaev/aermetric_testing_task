from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from aermetric.tests.factory import AircraftStatDataFactory


class GetAircraftStatDataAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.data_one = AircraftStatDataFactory(
            priority='Easy',
            type='Lower A',
            aircraft='AN923',
            status='In progress',
            errors_count=884,
            info_count=5
        )
        self.data_two = AircraftStatDataFactory(
            priority='Usual',
            type='Lower A',
            aircraft='AN923',
            status='Finished',
            errors_count=159,
            info_count=1
        )

    def test_get_stat_data(self):
        expected_data = [
            {"type": None, "aircraft": "AN923", "status": None, "errors_count": 1043, "info_count": 6, "lower_a": 2,
             "lower_b": 0, "paired_a": 0, "paired_b": 0, "upper_a": 0, "preLegend": 0, "legend": 0, "repeat_legend": 0,
             "warning": 0},
            {"type": None, "aircraft": None, "status": "Finished", "errors_count": 159, "info_count": 1, "lower_a": 1,
             "lower_b": 0, "paired_a": 0, "paired_b": 0, "upper_a": 0, "preLegend": 0, "legend": 0, "repeat_legend": 0,
             "warning": 0},
            {"type": None, "aircraft": None, "status": "In progress", "errors_count": 884, "info_count": 5,
             "lower_a": 1, "lower_b": 0, "paired_a": 0, "paired_b": 0, "upper_a": 0, "preLegend": 0, "legend": 0,
             "repeat_legend": 0, "warning": 0},
            {"type": "Lower A", "aircraft": None, "status": None, "errors_count": 1043, "info_count": 6, "lower_a": 2,
             "lower_b": 0, "paired_a": 0, "paired_b": 0, "upper_a": 0, "preLegend": 0, "legend": 0, "repeat_legend": 0,
             "warning": 0}
        ]

        response = self.client.get(
            reverse(
                'get_error_stats'
            ),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response.content, expected_data)
