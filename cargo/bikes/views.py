"""Views for Bikes app serializers."""

from rest_framework import viewsets
from bikes.models import Bike, Fleet
from bikes.serializers import BikeSerializer, FleetSerializer


class BikeViewSet(viewsets.ModelViewSet):
    """
    Viewset for Bike model. It includes all the REST methods, described below.

    retrieve:
    Return the given bike.

    list:
    Return a list of all the existing bikes.

    create:
    Create a new bike instance. It should be associated to a existent fleet.

    update:
    Update an existent bike instance. The informed id should be an integer.

    partial_update:
    Update an existent bike instance. The informed id should be an integer.

    delete:
    Delete an existent bike instance. The informed id should be an integer.
    """
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer


class FleetViewSet(viewsets.ModelViewSet):
    """
    Viewset for Fleet model. It includes all the REST methods, described below.

    retrieve:
    Return the given fleet.

    list:
    Return a list of all the existing fleets.

    create:
    Create a new fleet instance. It should be associated to a existent fleet.

    update:
    Update an existent fleet instance. The informed id should be an integer.

    partial_update:
    Update an existent fleet instance. The informed id should be an integer.

    delete:
    Delete an existent fleet instance. The informed id should be an integer.
    """
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer
