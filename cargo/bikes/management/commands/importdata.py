import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from bikes.models import Bike, Fleet


class Command(BaseCommand):
    help = 'Loads JSON data from Bikes and Fleets, and stores at the database.'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str,
                            help='Path of the JSON file to be loaded.')

    def add_bike(self, data):
        bike_data = {
            'id': Bike.get_int_id(data['id']),
            'fleet_id': Fleet.get_int_id(data['fleet']),
            'status': data['status'],
            'latitude': data['location']['latitude'],
            'longitude': data['location']['longitude'],
        }
        bike = Bike(**bike_data)
        bike.save()

    def add_fleet(self, data):
        fleet_data = {
            'id': Fleet.get_int_id(data['id']),
            'name': data['name'],
        }
        fleet = Fleet(**fleet_data)
        fleet.save()

    def handle(self, *args, **options):
        file = options['file']
        if not Path(file).is_file():
            raise CommandError('File not found')

        try:
            with open(file, 'r') as f:
                data = f.read()
            json_data = json.loads(data)

            for fleet_data in json_data['fleets']:
                self.add_fleet(fleet_data)
            for bike_data in json_data['bikes']:
                self.add_bike(bike_data)
        except Exception as e:
            raise CommandError(f'Unable to import objects. Error: {e}')

        self.stdout.write(self.style.SUCCESS('Successfully imported data'))
