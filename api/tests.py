from django.test import TestCase
from rest_framework.test import APIClient

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_calculate_route(self):
        data = {
            "uuid": "123e4567-e89b-12d3-a456-426614174000",
            "startPosition": {
                "longitude": 2.3522,
                "latitude": 48.8566
            },
            "parameters": {
                "optimizeForFuel": True,
                "optimizeForTime": False,
                "minimizeStops": False
            },
            "points": [
                {
                    "id": "1",
                    "designation": "Point A",
                    "longitude": 2.295,
                    "latitude": 48.8738
                },
                {
                    "id": "2",
                    "designation": "Point B",
                    "longitude": 2.333,
                    "latitude": 48.853
                }
            ],
            "averageSpeed": 60.0
        }
        response = self.client.post('/api/calculate-route/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_generate_map_url(self):
        data = {
            "uuid": "123e4567-e89b-12d3-a456-426614174000",
            "path": [
                {"longitude": 2.3522, "latitude": 48.8566},
                {"longitude": 2.295, "latitude": 48.8738},
                {"longitude": 2.333, "latitude": 48.853}
            ]
        }
        response = self.client.post('/api/generate-map-url/', data, format='json')
        self.assertEqual(response.status_code, 200)
