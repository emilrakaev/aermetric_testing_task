import factory

from aermetric.models import AircraftStatData


class AircraftStatDataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AircraftStatData
