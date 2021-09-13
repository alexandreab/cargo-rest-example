from rest_framework import status
from rest_framework.test import APITestCase

from bikes.models import Bike, Fleet


class TestFleet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = '/api/fleets/'

    def setUp(self):
        self.fleet_data = {
            "name": "Amsterdam",
        }

    def test_create_fleet(self):
        response = self.client.post(self.url, self.fleet_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_fleet(self):
        fleet_obj = Fleet.objects.create(**self.fleet_data)
        get_url = f'{self.url}{fleet_obj.id}/'
        response = self.client.get(get_url, self.fleet_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_json = {
            'id': 'FL_001',
            'name': 'Amsterdam'
        }
        self.assertEqual(response.json(), expected_json)

    def test_list_fleets(self):
        fleet_objs = list()
        for i in range(5):
            fleet_obj = Fleet.objects.create(**self.fleet_data)
            fleet_objs.append(fleet_obj)
        response = self.client.get(self.url, self.fleet_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 5)

    def test_delete_fleet(self):
        fleet_obj = Fleet.objects.create(**self.fleet_data)
        get_url = f'{self.url}{fleet_obj.id}/'
        response = self.client.delete(get_url, self.fleet_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(get_url, self.fleet_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestBike(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.url = '/api/bikes/'

    def setUp(self):
        self.fleet_obj = Fleet.objects.create(name="Amsterdam")

        self.bike_data = {
            "fleet": "FL_001",
            "status": "unlocked",
            "location": {
                "latitude": 52.08466738004343,
                "longitude": 4.3185523728791075
            },
        }

    def test_create_bike(self):
        response = self.client.post(self.url, self.bike_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_bike(self):
        bike_obj = Bike.objects.create(
            status="unlocked",
            latitude=52.08466738004343,
            longitude=4.3185523728791075,
            fleet_id=self.fleet_obj.id,
        )
        get_url = f'{self.url}{bike_obj.id}/'
        response = self.client.get(get_url, self.bike_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_json = {
            'fleet': 'FL_001',
            'status': 'unlocked',
            'location': {
                'latitude': 52.08466738004343,
                'longitude': 4.3185523728791075
            },
            'id': 'BK_001'
        }
        self.assertEqual(response.json(), expected_json)

    def test_list_bikes(self):
        bike_objs = list()
        for i in range(5):
            bike_obj = Bike.objects.create(
                status="unlocked",
                latitude=52.08466738004343,
                longitude=4.3185523728791075,
                fleet_id=self.fleet_obj.id,
            )
            bike_objs.append(bike_obj)
        response = self.client.get(self.url, self.bike_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 5)

    def test_delete_bike(self):
        bike_obj = Bike.objects.create(
            status="unlocked",
            latitude=52.08466738004343,
            longitude=4.3185523728791075,
            fleet_id=self.fleet_obj.id,
        )
        get_url = f'{self.url}{bike_obj.id}/'
        response = self.client.delete(get_url, self.bike_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(get_url, self.bike_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
