"""Serializers for Bikes app models."""

from rest_framework import serializers
from bikes.models import Bike, Fleet


class LocationField(serializers.Field):
    """Model serializer for location nested field from bike serializer."""

    def to_representation(self, value):
        return {
            "latitude": value.latitude,
            "longitude": value.longitude
        }

    def to_internal_value(self, data):
        return {
            "latitude": data['latitude'],
            "longitude": data['longitude']
        }


class BikeSerializer(serializers.ModelSerializer):
    """Model serializer Bike model."""

    location = LocationField(source='*')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = instance.str_id
        data['fleet'] = instance.fleet_str_id
        return data

    def to_internal_value(self, data):
        data['latitude'] = data['location']['latitude']
        data['longitude'] = data['location']['longitude']
        del data['location']
        data['fleet_id'] = Fleet.get_int_id(data['fleet'])
        del data['fleet']
        return data

    class Meta:
        model = Bike
        fields = ['fleet', 'status', 'location']
        read_only_fields = ['id']


class FleetSerializer(serializers.ModelSerializer):
    """Model serializer Fleet model."""

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = instance.str_id
        return data

    class Meta:
        model = Fleet
        fields = '__all__'
