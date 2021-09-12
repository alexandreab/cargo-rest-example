"""Models for Bikes app."""

from django.db import models


class Fleet(models.Model):
    """Fleet representation model. Its usually associated with a city."""
    name = models.CharField(max_length=15)

    @property
    def str_id(self):
        padded_id = str(self.id).zfill(3)
        return f'FL_{padded_id}'

    @staticmethod
    def get_int_id(str_value):
        return int(str_value.replace('FL_', ''))


class Bike(models.Model):
    """Bike representation model. Its always associated to a Fleet."""
    AVAILABLE_STATUS = (
        ('unlocked', 'Unlocked'),
        ('locked', 'Locked'),
    )
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=AVAILABLE_STATUS)
    latitude = models.FloatField()
    longitude = models.FloatField()

    @property
    def fleet_str_id(self):
        return self.fleet.str_id

    @property
    def str_id(self):
        padded_id = str(self.id).zfill(3)
        return f'BK_{padded_id}'

    @staticmethod
    def get_int_id(str_value):
        return int(str_value.replace('BK_', ''))
